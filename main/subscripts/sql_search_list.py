# Importē 'sqlite3' bibleotēkas 'connect' funkciju, kas ļauj savienoties ar .db failu.
from sqlite3 import connect

# Izveido funkciju 'query_sqldb', kas ļauj meklēt šķirkļus datubāzē..
def query_sqldb():

    # Izveido 'conn' mainīgo ar SQLite3 savienojumu failam 'sql.db'.
    conn = connect('data/sql.db')
    
    # Izveido 'cursor' mainīgo, ar kura palīdzību tiks pievienoti dati .db failam.
    cursor = conn.cursor()

    # Izvēlās 0 objektus no 'main_table' darba virsmas lai 'cursor' objektam būtu pieejams 'cursor.description' mainīgais.
    cursor.execute("SELECT * FROM main_table LIMIT 0")
    
    # Atrod visu kolonnu galvenes 'main_table' darba virsmā un saglabā tās.
    header = [description[0] for description in cursor.description]

    # Izveido LIKE nosacījumu katrai kolonnai.
    conditions = ["{} LIKE ?".format(column) for column in header]
    
    # Izveido WHERE operatora pieprasījumu, lai meklētu jebkuru atslēgvārdu jebkurā kolonnā.
    where_clause = " OR ".join(conditions)

    # Izveido SQL komandu 'query' string mainīgajā.
    query = "SELECT * FROM main_table WHERE " + where_clause

    # Sadala ievadu individuālos atslēgvārdos.
    for keyword in user_query.split():
        
        # Izpilda izveidoto meklēšanas pieprasījumu
        cursor.execute(query, tuple('%' + keyword + '%' for _ in header))
        
        # Atrod vienu izvēlēto rezultātu.
        output = cursor.fetchone()
        
        # Izmantojot 'close' funkciju, .db fails tiek aizvērts.
        conn.close()

        # Ja meklēšanā tika atrasts rezultāts, tad tas tiek izvadīts vārdnīcā.
        if output:
            query_results.append({'id': output[0], 'title': output[1], 'date': output[2], 'author': output[3], 'docs': output[4]})
        
        # Ja meklēšanā netika atrasts rezultāts, tad vārdnīcā tiek izvadīti 'empty' string mainīgie.
        else:
            query_results.append({'id': 'empty', 'title': 'empty', 'date': 'empty', 'author': 'empty', 'docs': 'empty'}) 

def main():
    query_sqldb()
    print(query_results)

if __name__ == "__main__":
    user_query = input("Query:")
    query_results = []
    main()
else:
    user_query = ""
    query_results = []
