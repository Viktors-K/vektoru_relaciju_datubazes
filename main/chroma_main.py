# Importē 'chromadb' bibleotēku, kas ļauj veidot vektordatubāzes.
import chromadb

# Izveido 'chroma_client' objektu.
chroma_client = chromadb.Client()

# Izveido 'collection' objektu, kurā tiks saglabāti iegulumi, dokumenti un citi papildus metadati. Kolekciju nosauc par "my_collection".
collection = chroma_client.create_collection(name="my_collection")

# Ar collection.add funkciju tiek pievienots dokuments kolekcijai.
collection.add(
    # Tiek definēti divi dokumenti.
    documents=["Abigail Gorlock", "Mike Oxlong", "Ben Dover", "Zobshavejs Zicelmanis Tresais"],
    # Tiek definēti papildus metadati šiem dokumentiem, šajā gadījumā 'source' informācija.
    metadatas=[{"source": "my_source"}, {"source": "my_source"}, {"source": "my_source"}, {"source": "my_source"}],
    # Tiek definēti dokumentu ID.
    ids=["id1", "id2", "id3", "id4"]
)
user_query = input("Query: (stop to leave)")
while (user_query != "stop"):

    # Izveido mainīgo 'results' ar kolecijas 'query' funkciju lai meklētu datubāzē.
    results = collection.query(
        # 'query' funkcijai tiek dots meklēšanas škirklis. 
        query_texts=[user_query],
        # 'query' funkcijai tiek dots vajadzīgais rezultātu daudzums, kas vistuvāk atbilst šķirklim. 
        n_results=4
    )

    # Izdrukā rezultātus no 'query' funkcijas.
    print(results)
    user_query = input("Query:")