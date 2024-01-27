# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

def query_sqldb(search_term):
    
    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'example.db'.
    conn = connect('data/sql.db')
    
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()
    
    # Izsauc SQL komandu lai izvēlētos visus attiecīgos rezultātus mainīgajam 'search_term'.
    cursor.execute("SELECT * FROM main_table WHERE column_name = ?", (search_term,))
    
    # Atrod visus izvēlētos rezultātus.
    rows = cursor.fetchall()
    
    # Izdrukā rezultātus
    if rows:
        print("Search Results:")
        for row in rows:
            print(row)
    else:
        print("No results found.")

    # Izmantojot 'close' funkciju, .db fails tiek aizvērts.
    conn.close()

# Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
user_query = input("Query:")

# Izpilda 'query_sqldb funkciju ar lietotāja ievadu.'
query_sqldb(user_query)