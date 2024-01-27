# Importē 'csv' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from csv import reader

# Importē 'sqlite3' bibleotēkas 'reader' objektu, kas ļauj lasīt .csv tipa failus.
from sqlite3 import connect



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

# Function to create SQLite database and insert data
def create_db_from_csv(csv_file, db_file, table_name):

    # Read data from CSV
    csv_data = import_data(csv_file)
    
    # Connect to SQLite database
    conn = connect(db_file)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(csv_data[0])})")
    
    # Insert data into table
    for row in csv_data[1:]:
        placeholders = ', '.join(['?' for _ in row])
        cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Example usage
csv_file_path = '../data/first.csv'
db_file_path = '../data/example2.db'
table_name = 'main_table'

create_db_from_csv(csv_file_path, db_file_path, table_name)