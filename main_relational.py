# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

# Importē 'save_to_csv' faila 'save' funkciju, kas saglabā izveidotos datus .csv failā, un funkciju 'start_results', kas pievieno datiem sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
from subscripts.save_to_csv import save,start_results

### Importē 'save_to_csv' faila 'save' funkciju, kas saglabā izveidotos datus .csv failā, un funkciju 'start_results', kas pievieno datiem sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
from subscripts.import_sql import create_db_from_csv

create_db_from_csv('first.csv', 'data/sql.db')

# Izveido mainīgo 'times_repeated', kas iedod ievada iespēju lietotājam lai iestatīt cik reizes atkārtot laika mērīšanu.
times_repeated = int(input("Cik reizes veikt atkārtotu laika mērīšanu: "))

# Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
user_query = input("Query:")

# Izveido tukšu sarakstu 'query_results' kurā tiks pievienoti rezultāti no katras meklēšanas funkcijas izsaukšanas.
query_results = []

# Izveido jaunu sarakstu 'data' ar sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
data = start_results(times_repeated,user_query, 'relational')

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
        data.append([i+1,time_taken_ms,query_results[i]['id'],query_results[i]['docs'],query_results[i]['source']])

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

# Izveido funkciju 'query_sqldb' ar 1 ievadu 'req_func', kas pieņem string mainīgo, ko izmantot kā meklēšanas škirkli.
def query_sqldb():
    
    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'sql.db'.
    conn = connect('data/sql.db')
    
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()
    
    # Izvēlās 0 objektus no 'main_table' darba virsmas lai 'cursor' objektam būtu pieejams 'cursor.description' mainīgais.
    cursor.execute("SELECT * FROM main_table LIMIT 0")
    
    # Iesāk SQL komandu 'query' string mainīgajā.
    query = "SELECT * FROM main_table WHERE "
    
    # Atrod visu kolonnu galvenes 'main_table' darba virsmā un saglabā tās.
    header = [description[0] for description in cursor.description]
    
    # Izveido LIKE nosacījumu katrai kolonnai.
    conditions = ["{} LIKE ?".format(column) for column in header]
    
    # Savieno galvenes ar OR nosacījumu, lai katra kolonna ir meklējama.
    query += " OR ".join(conditions)
    
    # Izsauc SQL komandu lai izvēlētos visus attiecīgos rezultātus mainīgajam 'user_query' visās kolonnās.
    cursor.execute(query, ('%' + user_query + '%',) * len(header))
    
    # Atrod vienu izvēlēto rezultātu.
    output = cursor.fetchone()
    
    # Izmantojot 'close' funkciju, .db fails tiek aizvērts.
    conn.close()
    
    # Ja meklēšanā tika atrasts rezultāts, tad tas tiek izvadīts vārdnīcā.
    if output:
        query_results.append({'id':f'{output[0]}','docs':f'{output[1]}','source':f'{output[2]}'})
    
    # Ja meklēšanā netika atrasts rezultāts, tad vārdnīcā tiek izvadīti 'empty' string mainīgie.
    else:
        query_results.append({'id':'empty','docs':'empty','source':'empty'})

# Izsauc un saglabā kolekcijas meklēšanas pieprasījuma laika rezultātus.
exported_data = measure(query_sqldb, times_repeated, data)
save(exported_data)
