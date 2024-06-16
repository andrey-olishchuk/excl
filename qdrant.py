import os
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import Distance, VectorParams

qdrant_url = os.environ.get("QDRANT_URL", "http://localhost:6333")
qdrant_collection = os.environ.get("QDRANT_COLLECTION", "knowledgebase")

client = QdrantClient(url=qdrant_url)

def add_index(i, vector, link, source, altcollection=False):
    collection = qdrant_collection if altcollection==False else altcollection
    upsert = client.upsert(
        collection_name=collection,
        wait=True,
        points=[
            PointStruct(id=i, vector=vector, payload={"source": source, "link": link})
        ],
    )
    return upsert

def search(vector):
    result = client.search(
        collection_name=qdrant_collection,
        query_vector=vector,
        limit=3,
    )
    return result

def kickoff(collection):
    result = client.create_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=768, distance=Distance.DOT),
    )
    return result