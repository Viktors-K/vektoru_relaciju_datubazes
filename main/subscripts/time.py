# Importē 'timeit' bibleotēkas 'timeit' funkciju, kas ļauj izmērīt vajadzīgo laiku funkcijas izpildei.
from timeit import timeit 

# Izveido funkciju 'relational_function' kas iesāk relāciju datubāzes meklēšanu, šobrīd, bez koda, izmēģinājumiem.
def relational_function():
    pass

times_repeated = int(input("Cik reizes veikt atkārtotu laika mērīšanu: "))
total_time_ms = 0

for i in range(0,times_repeated):
    print(f"Repetition number {i+1}")
# Izveido jaunu mainīgo 'time_taken', kas izmanto 'timeit' bibleotēkas funkciju lai izmērītu cik ilgu laiku aizņems izpildīt 250000 pieprasījumus 'relational_function' funkcijai.
    time_taken = timeit(relational_function, number=250000)
# Izveido jaunu mainīgo 'time_taken_ms', kas reizina mainīgo 'time_taken' 1000 reizes lai iegūtu rezultātu milisekundēs un to noapaļo līdz 5-1=4 skaitļiem aiz komata.
    time_taken_ms = round(time_taken*1000, 5)
    # Izdrukā konsolē gan aizņemto laiku sekundēs, gan milisekundēs
    print(f"Time taken: {time_taken} seconds")
    print(f"Time taken: {time_taken_ms} miliseconds")
    total_time_ms = total_time_ms + time_taken_ms

print("_______________________________________________________________")
avg_time_ms = round(total_time_ms / times_repeated,5)
print(f"Average time taken: {avg_time_ms} miliseconds")

