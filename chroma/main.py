import chromadb
from chromadb.utils import embedding_functions
default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["This is a document", "This is another document"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2"]
)
collection.add(
    documents=["dog", "cat"],
    val = default_ef("cat")
    print(val)
    #embeddings=[[default_ef(["dog"])],[default_ef(["cat"])]]
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id3", "id4"]
)
collection.add(
    documents=["edgar allan poe", "renards roze"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
    ids=["id5", "id6"]
)


results = collection.query(
    query_texts=["charles darwin"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)

print(results)