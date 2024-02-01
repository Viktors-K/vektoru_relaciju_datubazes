# Importē 'csv' bibleotēkas 'writer' objektu, kas ļauj veidot un rakstīt .csv tipa failus.
from csv import writer
# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import makedirs
from os import path
# Importē 'datetime' bibleotēkas 'datetime' funkcijas, kas ļauj saglabāt šobrīdējo laiku un to formatēt.
from datetime import datetime

# Izmantojot datetime bibleotēku izveido string mainīgo, kurā saglabāts šobrīdējais datums un laiks faila nosaukumam. 
current_timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

# Definē datus, kam jābut saglabātiem
data = [
    ["Name", "Age", "Occupation"],
    ["John", 30, "Engineer"],
    ["Jane", 25, "Doctor"],
    ["Bob", 35, "Teacher"]
]

# Izveido faila nosaukuma mainīgo.
file_name =  (f"{current_timestamp}.csv")

# Izveido faila lokācijas mainīgo.
file_path = path.join(path.dirname(__file__), 'results', file_name)

# Izveido faila lokācijas mainīgo.
makedirs(path.dirname(file_path), exist_ok=True)

# Atver failu ar nosaukumu 'file_name' un tajā ieraksta visu kas ir 'data' objektā.
with open(file_path, mode='w', newline='') as file:
    writer = writer(file)
    writer.writerows(data)

# Izdrukā konsolē paziņojumu par saglabātajiem rezultātiem un kur tie ir saglabāti.
print(f"Data has been saved to {file_path}")


