import requests
import chromadb
from sentence_transformers import SentenceTransformer
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8520330001:AAHMaZoWcAK8UjsogIRI6kRf1eE-3oQwJRI"

client = chromadb.Client()
collection = client.get_collection("mastic")

embedder = SentenceTransformer(
"sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

OLLAMA_URL = "http://localhost:11434/api/generate"

def search_knowledge(question):
    emb = embedder.encode([question])[0]

    results = collection.query(
        query_embeddings=[emb],
        n_results=3
    )

    return "\n".join(results["documents"][0])


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = update.message.text

    context_text = search_knowledge(question)

    prompt = f"""
Απάντησε μόνο με βάση το εγχειρίδιο μαστίχας.

Εγχειρίδιο:
{context_text}

Ερώτηση:
{question}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model":"openeurollm-greek",
            "prompt":prompt,
            "stream":False
        }
    )

    answer = r.json()["response"]

    await update.message.reply_text(answer)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()