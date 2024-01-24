# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

# Importē 'sys' bibleotēkas 'version_info' funkciju, kas ļauj pārbaudīt izmantoto Python versiju.
from sys import version_info

# Importē 'csv' bibleotēkas 'writer' objektu, kas ļauj veidot un rakstīt .csv tipa failus.
from csv import writer

# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import makedirs
from os import path

# Importē 'datetime' bibleotēkas 'datetime' funkcijas, kas ļauj saglabāt šobrīdējo laiku un to formatēt.
from datetime import datetime

# Izveido mainīgo 'py_version' kas saglabā izmantoto Python versiju datu saglabāšanai.
py_version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

# Izveido funkciju 'relational_function' kas iesāk relāciju datubāzes meklēšanu, šobrīd, bez koda, izmēģinājumiem.
def relational_function():
    pass

# Izveido mainīgo 'times_repeated' kas iedod ievada iespēju lietotājam lai iestatīt cik reizes atkārtot laika mērīšanu.
times_repeated = int(input("Cik reizes veikt atkārtotu laika mērīšanu: "))

# Izveido mainīgo 'multiplier' ar sākuma daudzumu 250000, kas izmantots 'timeit' funkcijā kā reizinātājs lai noteiktu cik reizes izpildīt funkciju.
multipilier = 250000

# Izmantojot datetime bibleotēku izveido string mainīgo, kurā saglabāts šobrīdējais datums un laiks faila nosaukumam. 
current_timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

# Izveido funkciju 'measure' ar 3 ievadiem, 'req_func', kas pieņem funkciju, ko mērīt, 'req_multiplier', kas pieņem skaitli, kuru izmantot 'timeit' funkcijas reizinātājam un 'repeated', kas pieņem skaitli, kurš nosaka cik reizes atkārtot mērījumus.
def measure(req_func,req_multiplier,repeated):
    # Izveido mainīgo 'func_total_time_ms' ar sākuma daudzumu 0, kurā vēlāk tiks saglabāts milisekunžu skaits kopā, kas vajadzīgs funkciju izpildei.
    func_total_time_ms = 0
    # Definē 'data' sarakstu, ar sākuma datiem un formatēšanu.
    data = [
        ["Datums","Laiks", "Atkartotas reizes"],
        # Ievada šobrīdējo datumu, laiku un saglabā 'repeated' mainīgo.
        [datetime.now().strftime('%d-%m-%Y'),datetime.now().strftime('%H:%M:%S'),repeated],
        ["Atkartojuma nr.p.k.", "Reizinatajs", "Laiks (ms)"]
    ]
    # Cikls, kas veic mērīšanu 'repeated' reizes.
    for i in range(0,repeated):
        # Izveido jaunu mainīgo 'time_taken', kas izmanto 'timeit' bibleotēkas funkciju lai izmērītu cik ilgu laiku aizņems izpildīt 'req_multiplier' reizes 'req_func' funkciju.
        time_taken = timeit(req_func, number=req_multiplier)
        # Izveido jaunu mainīgo 'time_taken_ms', kas reizina mainīgo 'time_taken' 1000 reizes lai iegūtu rezultātu milisekundēs un to noapaļo līdz 5-1=4 skaitļiem aiz komata.
        time_taken_ms = round(time_taken*1000, 5)
        # Pievieno 'data' sarakstam atkārtojuma nr.p.k., attiecīgo reizinātāju un cik milisekundes funkcija aizņēma.
        data.append([i+1,req_multiplier,time_taken_ms])
        # Pēc katras funkcijas nomērīšanas pievieno aizņemto laiku 'func_total_time_ms' mainīgajam lai saglabātu cik laika visas funkcijas atkārtošanas reizes aizņēma.
        func_total_time_ms = func_total_time_ms + time_taken_ms
    # Izrēķina vidējo patērēto laiku vienai funkcijas nomērīšanai un to noapaļo līdz 5-1=4 skaitļiem aiz komata.
    avg_time_ms = round(func_total_time_ms / repeated,5)
    # Pievieno tukšu rindu 'data' sarakstam
    data.append([])
    # Pievieno 'data' sarakstam kopējo funkciju laiku un vidējo funkciju laiku milisekundēs.
    data.append(['Kopejais funkciju laiks (ms)','Videjais funkciju laiks (ms)'])
    data.append([func_total_time_ms,avg_time_ms])
    return data

# Izveido funkciju 'save' ar 2 ievadiem, 'timestamp', kas pieņem string mainīgo laika posma saglabāšanai, kā arī 'info', kas pieņem sarakstu .csv faila izveidei un saglabāšanai.
def save(timestamp, info):
    
    # Izveido faila nosaukuma mainīgo ar ievadīto datumu un laiku.
    file_name =  (f"{timestamp}.csv")

    # Izveido faila lokācijas mainīgo.
    file_path = path.join(path.dirname(__file__), 'results', file_name)

    # Izveido faila lokācijas mainīgo.
    makedirs(path.dirname(file_path), exist_ok=True)

    # Atver failu ar nosaukumu 'file_name' un tajā ieraksta visu kas ir 'info' objektā.
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer_instance = writer(file)
        writer_instance.writerows(info)

    # Izdrukā konsolē paziņojumu par saglabātajiem rezultātiem un kur tie ir saglabāti.
    print(f"Data has been saved to {file_path}")

exported_data = measure(relational_function, multipilier, times_repeated)
save(current_timestamp,exported_data)
