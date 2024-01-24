# Importē 'chromadb' bibleotēku, kas ļauj veidot vektordatubāzes.
import chromadb

# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import path

# Importē 'csv' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from csv import reader

# Definē funkciju 'import_data' ar vienu ievadu, 'db_file_name', kas pieņem string mainīgo vajadzīgā faila nosaukumam.
def import_data(db_file_name):
    # Izveido sākuma datu faila lokācijas mainīgo 'db_file_path'.
    db_file_path = path.join(path.dirname(__file__), 'data', db_file_name)

    # Izveido tukšu sarakstu 'db_data' kurā tiks pievienoti dati no sākuma datu faila.
    db_data = []

    # Atver un nolasa sākuma datu .csv failu.
    with open(db_file_path) as db_csv:
        # Izveido .csv faila lasītāja objektu
        csv_reader = reader(db_csv)
        # Izlaiž pirmo galvenes rindu, ja tā eksistē.
        header = next(csv_reader, None)
        # Pievieno katru rindu no .csv faila 'db_data' sarakstam
        for row in csv_reader:
            db_data.append(row)

    # Izveido 3 tukšus sarakstus ChromaDB formatēšanai
    ids = []
    names = []
    sources = []

    # Pievieno visus ID, vārdus un avotus savos sarakstos ChromaDB formatēšanai
    for row in db_data:
        ids.append(row[0])
        names.append(row[1])
        sources.append(row[2])

    # Izdrukā formatētos datus
    return (ids,names,sources)
    

imported_data = import_data('first.csv')
imported_ids = imported_data[0]
imported_docs = imported_data[1]
imported_metadata = [{'source': value} for value in imported_data[2]]

# Izveido 'chroma_client' objektu.
chroma_client = chromadb.Client()

# Izveido 'collection' objektu, kurā tiks saglabāti iegulumi, dokumenti un citi papildus metadati. Kolekciju nosauc par "my_collection".
collection = chroma_client.create_collection(name="my_collection")

# Ar collection.add funkciju tiek pievienota informācija kolekcijai.
collection.add(
    # Tiek definēti divi dokumenti.
    documents=imported_docs,
    # Tiek definēti papildus metadati šiem dokumentiem, šajā gadījumā 'source' informācija.
    metadatas=imported_metadata,
    # Tiek definēti dokumentu ID.
    ids=imported_ids
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