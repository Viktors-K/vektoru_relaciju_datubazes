# Importē 'csv' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from csv import reader

# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

# Importē 'os' bibleotēkas 'path' funkciju, kas ļauj formatēt direktorijas.
from os import path

# Definē funkciju 'import_data' ar vienu ievadu, 'db_file_name', kas pieņem string mainīgo vajadzīgā faila nosaukumam.
def import_data(db_file_name):
    
    # Izveido sākuma datu faila lokācijas mainīgo 'db_file_path'.
    db_file_path = path.join(path.dirname(__file__), '..', 'data', db_file_name)

    # Izveido tukšu sarakstu 'db_data' kurā tiks pievienoti dati no sākuma datu faila.
    db_data = []

    # Atver un nolasa sākuma datu .csv failu.
    with open(db_file_path) as db_csv:
        
        # Izveido .csv faila lasītāja objektu
        csv_reader = reader(db_csv)
        
        # Izlaiž pirmo galvenes rindu, ja tā eksistē.
        header = next(csv_reader, None)
        
        # Pievieno katru rindu no .csv faila 'db_data' sarakstam.
        for row in csv_reader:
            db_data.append(row)

    # Izvada nolasīto informāciju no .csv faila saraksta objektā.
    return db_data

# Definē funkciju 'create_db_from_csv' ar diviem ievadiem, 'csv_file', kas pieņem string mainīgo sākuma datu faila nosaukumam un 'db_file', kas pieņem string mainīgo beigu DB faila nosaukumam.
def create_db_from_csv(csv_file, db_file):
    # Izsauc  funkciju 'import_data' un ievada tās izvadu sarakstā 'csv_data'.
    csv_data = import_data(csv_file)

    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'db_file'.
    conn = connect(db_file)
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()
    
    # Izsauc SQL komandu lai izveidotu jaunu darba virmsu 'main_table' .db failā un pievieno pirmo rindu no .csv faila kā galveni darba virsmai.
    cursor.execute(f"CREATE TABLE IF NOT EXISTS main_table ({', '.join(csv_data[0])})")
    
    # Pievieno katru rindu no .csv faila 'main_table' darba virsmā.
    for row in csv_data[1:]:
        placeholders = ', '.join(['?' for _ in row])
        cursor.execute(f"INSERT INTO main_table VALUES ({placeholders})", row)

    # Izmantojot 'commit' funkciju, izmaiņas tiek apstiprinātas un ar 'close' funkciju, .db fails tiek aizvērts.
    conn.commit()
    conn.close()

create_db_from_csv('first.csv', 'data/sql.db')