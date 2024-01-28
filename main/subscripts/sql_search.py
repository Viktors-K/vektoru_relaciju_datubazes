# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

# Izveido funkciju 'query_sqldb' ar 1 ievadu 'req_func', kas pieņem string mainīgo, ko izmantot kā meklēšanas škirkli.
def query_sqldb(search_term):
    
    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'sql.db'.
    conn = connect('data/sql.db')
    
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()
    
    # Izvēlās 0 objektus no 'main_table' darba virsmas lai 'cursor' objektam būtu pieejams 'cursor.description' mainīgais.
    cursor.execute("SELECT * FROM main_table LIMIT 0")
    
    # Iesāk SQL komandu 'query' string mainīgajā.
    query = "SELECT * FROM main_table WHERE "
    
    # Atrod visu kolonnu galvenes 'main_table' darba virsmā un saglabā tās.
    header = [description[0] for description in cursor.description]
    
    # Izveido LIKE nosacījumu katrai kolonnai.
    conditions = ["{} LIKE ?".format(column) for column in header]
    
    # Savieno galvenes ar OR nosacījumu, lai katra kolonna ir meklējama.
    query += " OR ".join(conditions)
    
    # Izsauc SQL komandu lai izvēlētos visus attiecīgos rezultātus mainīgajam 'search_term' visās kolonnās.
    cursor.execute(query, ('%' + search_term + '%',) * len(header))
    
    # Atrod vienu izvēlēto rezultātu.
    output = cursor.fetchone()
    
    # Izmantojot 'close' funkciju, .db fails tiek aizvērts.
    conn.close()
    
    # Ja meklēšanā tika atrasts rezultāts, tad tas tiek izvadīts vārdnīcā.
    if output:
        return {'id':f'{output[0]}','docs':f'{output[1]}','source':f'{output[2]}'}
    
    # Ja meklēšanā netika atrasts rezultāts, tad vārdnīcā tiek izvadīti 'empty' string mainīgie.
    else:
        return {'id':'empty','docs':'empty','source':'empty'}

# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():

    # Izveido mainīgo 'user_query', kas iedod ievada iespēju lietotājam lai iestatīt meklēšanas šķirkli.
    user_query = input("Query:")

    # Izpilda 'query_sqldb funkciju ar lietotāja ievadu.'
    print(query_sqldb(user_query))

# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    main()
    
