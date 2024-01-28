# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

# Importē 'save_to_csv' faila 'save' funkciju, kas saglabā izveidotos datus .csv failā, un funkciju 'start_results', kas pievieno datiem sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
from subscripts.save_to_csv import save,start_results

# Importē 'chromadb_main' faila 'create_collection' funkciju, kas izveido kolekcijas objektā vektordatubāzi.
from subscripts.chromadb_main import create_collection

# Izveido mainīgo 'times_repeated', kas iedod ievada iespēju lietotājam lai iestatīt cik reizes atkārtot laika mērīšanu.
times_repeated = int(input("Cik reizes veikt atkārtotu laika mērīšanu: "))

# Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
user_query = input("Query:")

# Izveido jaunu sarakstu 'data' ar sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
data = start_results(times_repeated,user_query)

# Izveido tukšu sarakstu 'query_results' kurā tiks pievienoti rezultāti no katras meklēšanas funkcijas izsaukšanas.
query_results = []

# Izveido funkciju 'measure' ar 3 ievadiem, 'req_func', kas pieņem funkciju, ko mērīt, 'repeated', kas pieņem skaitli, kurš nosaka cik reizes atkārtot mērījumus un 'data', kas pieņem iesāktu sarakstu lai tam var pievienot datus.
def measure(req_func,repeated, data):
    
    # Izveido mainīgo 'func_total_time_ms' ar sākuma daudzumu 0, kurā vēlāk tiks saglabāts milisekunžu skaits kopā, kas vajadzīgs funkciju izpildei.
    func_total_time_ms = 0

    # Cikls, kas veic mērīšanu 'repeated' reizes.
    for i in range(0,repeated):

        # Izveido jaunu mainīgo 'time_taken', kas izmanto 'timeit' bibleotēkas funkciju lai izmērītu cik ilgu laiku aizņems izpildīt 1 reizi 'req_func' funkciju.
        time_taken = timeit(req_func, number=1)

        # Izveido jaunu mainīgo 'time_taken_ms', kas reizina mainīgo 'time_taken' 1000 reizes lai iegūtu rezultātu milisekundēs un to noapaļo līdz 5-1=4 skaitļiem aiz komata.
        time_taken_ms = round(time_taken*1000, 5)

        # Pievieno 'data' sarakstam atkārtojuma nr.p.k., attiecīgo reizinātāju un cik milisekundes funkcija aizņēma.
        data.append([i+1,time_taken_ms,query_results[i]])

        # Pēc katras funkcijas nomērīšanas pievieno aizņemto laiku 'func_total_time_ms' mainīgajam lai saglabātu cik laika visas funkcijas atkārtošanas reizes aizņēma.
        func_total_time_ms = func_total_time_ms + time_taken_ms

    # Izrēķina vidējo patērēto laiku vienai funkcijas nomērīšanai un to noapaļo līdz 5-1=4 skaitļiem aiz komata.
    avg_time_ms = round(func_total_time_ms / repeated,5)

    # Pievieno tukšu rindu 'data' sarakstam vieglākai rezultātu nolasīšanai.
    data.append([])

    # Pievieno 'data' sarakstam kopējo funkciju laiku un vidējo funkciju laiku milisekundēs.
    data.append(['Kopejais funkciju laiks (ms)','Videjais funkciju laiks (ms)'])
    data.append([func_total_time_ms,avg_time_ms])

    # Izvada visus formatētos datus vēlākai rezultātu saglabāšanai saraksta objektā.
    return data

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
