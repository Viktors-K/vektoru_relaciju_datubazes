# Importē 'chromadb' bibleotēku, kas ļauj veidot vektordatubāzes.
from chromadb import Client

# Definē funkciju 'create_collection' ar vienu ievadu, 'db_file_name', kas pieņem string mainīgo vajadzīgā faila nosaukumam.
def create_collection(db_file_name):
    
    # Izveido 'imported_data' objektu, kurā ievadīti visi dati no 'db_file_name' faila.
    imported_data = import_data(db_file_name, 'vector')
    
    # Izveido 3 tukšus sarakstus ChromaDB formatēšanai
    imported_ids = []
    imported_docs = []
    imported_sources = []
   
    # Pievieno visus ID, vārdus un avotus savos sarakstos ChromaDB formatēšanai
    for row in imported_data:
        imported_ids.append(row[0])
        imported_docs.append(row[1])
        imported_sources.append(row[2])

    # Pārveido importēto 'source' informāciju vārdnīcā ChromaDB formatēšanai
    imported_metadata = [{'source': value} for value in imported_sources]

    # Izveido 'chroma_client' objektu.
    chroma_client = Client()

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

    # Izvada izveidoto kolekciju ar datiem ChromaDB kolekcijas objektā.
    return collection

# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():
    
    # Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
    user_query = input("Query:")
    
    # Izveido jaunu kolekciju 'collection' objektā.
    collection = create_collection('first.csv')

    # Izveido mainīgo 'results' ar kolecijas 'query' funkciju lai meklētu datubāzē.
    results = collection.query(
        
        # 'query' funkcijai tiek dots meklēšanas škirklis. 
        query_texts=[user_query],
        
        # 'query' funkcijai tiek dots vajadzīgais rezultātu daudzums, kas vistuvāk atbilst šķirklim. 
        n_results=1
    )
    
    # Izsauc un izdrukā kolekcijas meklēšanas pieprasījuma rezultātus.
    print(results['documents'])

# Ja atvērts netieši, šis skripts importēs ārēji 'import_data' faila funkciju.
if __name__ != "__main__":
    # Importē 'import_data' faila 'import_data' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
    from subscripts.import_data import import_data
    
# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    # Importē 'import_data' faila 'import_data' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
    from import_data import import_data
    main()