# Importē 'csv' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from csv import reader


# Definē funkciju 'import_data' ar vienu ievadu, 'db_file_name', kas pieņem string mainīgo vajadzīgā faila nosaukumam.
def import_data(db_file_name):

    # Izveido tukšu sarakstu 'db_data' kurā tiks pievienoti dati no sākuma datu faila.
    db_data = []

    # Atver un nolasa sākuma datu .csv failu.
    with open(db_file_name) as db_csv:
        
        # Izveido .csv faila lasītāja objektu
        csv_reader = reader(db_csv)
        
        # Izlaiž pirmo galvenes rindu, ja tā eksistē.
        header = next(csv_reader, None)
        
        # Pievieno katru rindu no .csv faila 'db_data' sarakstam
        for row in csv_reader:
            db_data.append(row)

    # Izvada nolasīto informāciju no .csv faila saraksta objektā.
    return db_data

print(import_data('data/first.csv'))
