# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import path



from csv import reader

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
    

print(import_data('first.csv'))