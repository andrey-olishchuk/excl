import os
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

qdrant_url = os.environ.get("QDRANT_URL", "http://localhost:6333")
qdrant_collection = os.environ.get("QDRANT_COLLECTION", "knowledgebase")

client = QdrantClient(url=qdrant_url)

def add_index(i, vector, link, source):
    upsert = client.upsert(
        collection_name=qdrant_collection,
        wait=True,
        points=[
            PointStruct(id=i, vector=vector, payload={"source": source, "link": link})
        ],
    )
    return upsert