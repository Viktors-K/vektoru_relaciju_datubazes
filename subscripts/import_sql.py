# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

# Definē funkciju 'create_db_from_csv' ar diviem ievadiem, 'csv_file', kas pieņem string mainīgo sākuma datu faila nosaukumam un 'db_file', kas pieņem string mainīgo beigu DB faila nosaukumam.
def create_db_from_csv(csv_file, db_file):
    
    # Definē funkciju 'row_exists' ar diviem ievadiem, 'cursor', kas pieņem cursor objektu un 'row', kas pieņem sarakstu, lai pārbaudītu vai tāda rinda darba virsmā jau ir pievienots.
    def row_exists(cursor, row):
        cursor.execute("SELECT EXISTS(SELECT 1 FROM main_table WHERE " + " AND ".join(f"{header[i]} = ?" for i in range(len(header))) + ")", row)
        return cursor.fetchone()[0]
    
    # Izsauc  funkciju 'import_data' un ievada tās izvadu sarakstā 'csv_data'.
    imported_data = import_data(csv_file, 'relational')
    
    # Iestata 'header' mainīgo uz pirmo mainīgo sarakstā, kas ir galvene.
    header = imported_data[0]
    
    # Iestata 'csv_data' mainīgo uz otro mainīgo sarakstā, kas ir pārējie dati.
    csv_data = imported_data[1]
    
    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'db_file'.
    conn = connect(db_file)
    
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()
    
    # Izsauc SQL komandu lai izveidotu jaunu darba virmsu 'main_table' .db failā un pievieno pirmo rindu no .csv faila kā galveni darba virsmai.
    cursor.execute(f"CREATE TABLE IF NOT EXISTS main_table ({', '.join(header)})")
    
    # Pievieno katru rindu no .csv faila 'main_table' darba virsmā, ja tā nav jau pievienota.
    for row in csv_data:
        if not row_exists(cursor, row):
            placeholders = ', '.join(['?' for _ in row])
            cursor.execute(f"INSERT INTO main_table VALUES ({placeholders})", row)

    # Izmantojot 'commit' funkciju, izmaiņas tiek apstiprinātas un ar 'close' funkciju, .db fails tiek aizvērts.
    conn.commit()
    conn.close()

# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():
    # Izsauc 'create_db_from_csv' funkciju, importējot datus no 'first.csv' un saglabājot tos 'data/sql.db'.
    create_db_from_csv('first.csv', 'data/sql.db')

# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    
    # Importē 'import_data' faila 'import_data' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
    from import_data import import_data
    
    main()
else:
    # Importē 'import_data' faila 'import_data' funkciju, kas importē datus no dota .csv faila nosaukuma un izvada tos sarakstā.
    from subscripts.import_data import import_data

