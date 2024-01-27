# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

# Importē 'sys' bibleotēkas 'version_info' funkciju, kas ļauj pārbaudīt izmantoto Python versiju.
from sys import version_info

# Importē 'csv' bibleotēkas 'writer' objektu, kas ļauj veidot un rakstīt .csv tipa failus.
from csv import writer

# Importē 'csv' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from csv import reader

# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import makedirs
from os import path

# Importē 'chromadb' bibleotēku, kas ļauj veidot vektordatubāzes.
from chromadb import Client

# Importē 'datetime' bibleotēkas 'datetime' funkcijas, kas ļauj saglabāt šobrīdējo laiku un to formatēt.
from datetime import datetime

# Importē 'import_data' faila 'import_data' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
from subscripts.import_data import import_data

### Importē '' faila '' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
from subscripts.save_to_csv import save,start_results


### Importē '' faila '' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
from subscripts.measure import measure

### Importē '' faila '' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
from subscripts.chromadb_main import create_collection

# Importē 'version.py' failu, kas izveido mainīgo py_version ar šobrīdējo Python versiju.
import subscripts.version
# Izveido mainīgo 'times_repeated', kas iedod ievada iespēju lietotājam lai iestatīt cik reizes atkārtot laika mērīšanu.
times_repeated = int(input("Cik reizes veikt atkārtotu laika mērīšanu: "))

# Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
user_query = input("Query:")

# Izveido tukšu sarakstu 'query_results' kurā tiks pievienoti rezultāti no katras meklēšanas funkcijas izsaukšanas.
query_results = []
print(subscripts.version.py_version)
###
data = start_results(times_repeated,user_query, subscripts.version.py_version)

# Izveido tukšu sarakstu 'query_results' kurā tiks pievienoti rezultāti no katras meklēšanas funkcijas izsaukšanas.
query_results = []

# Definē funkciju 'query_vectordb', kas izmanto 'user_query' string mainīgo meklēšanas šķirklim.
def query_vectordb():
    
    # Izveido mainīgo 'results' ar kolecijas 'query' funkciju lai meklētu datubāzē.
    results = collection.query(
        
        # 'query' funkcijai tiek dots meklēšanas škirklis. 
        query_texts=[user_query],
        
        # 'query' funkcijai tiek dots vajadzīgais rezultātu daudzums, kas vistuvāk atbilst šķirklim. 
        n_results=1
    )
    
    # Izdrukā rezultātus no 'query' funkcijas.
    doc = str(results['documents'])
    query_results.append(doc[3:-3])

# Izveido jaunu kolekciju 'collection' objektā.
collection = create_collection('first.csv')

# Izsauc un saglabā kolekcijas meklēšanas pieprasījuma laika rezultātus.
exported_data = measure(query_vectordb, times_repeated, data)
save(exported_data)
