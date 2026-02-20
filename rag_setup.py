import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.create_collection("mastic")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

text = open("manual.txt",encoding="utf-8").read()

chunks = [text[i:i+800] for i in range(0,len(text),800)]

embeddings = model.encode(chunks)

for i,chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        embeddings=[embeddings[i]],
        ids=[str(i)]
    )

print("Knowledge uploaded")