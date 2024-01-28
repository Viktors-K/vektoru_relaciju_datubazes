# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

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




# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():
    # Izveido piemēra funkciju 'example_function'
    def example_function():
        pass
    # Izdrukā importētos datus no 'first.csv'
    print(measure(example_function,1,int(input("Cik reizes atkārtot mērīšanu: "))))

# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    main()