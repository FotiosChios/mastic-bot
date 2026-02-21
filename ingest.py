from pypdf import PdfReader
import chromadb
from sentence_transformers import SentenceTransformer

print("Reading PDF...")

reader = PdfReader("manual.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print("Creating chunks...")

chunk_size = 800
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print("Loading embedding model...")

embedder = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

print("Creating database...")

client = chromadb.Client()
collection = client.create_collection("mastic")

# Batch encode all chunks at once (efficient!)
embeddings = embedder.encode(chunks)

for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        embeddings=[embeddings[i]],  # Use pre-computed embedding
        ids=[str(i)]
    )

print("DONE — knowledge stored.")
