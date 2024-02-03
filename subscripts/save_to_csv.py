# Importē 'csv' bibleotēkas 'writer' objektu, kas ļauj veidot un rakstīt .csv tipa failus.
from csv import writer

# Importē 'os' bibleotēkas 'makedirs' un 'path' funkciju, kas ļauj izveidot direktorijas kā arī tās formatēt.
from os import makedirs
from os import path

# Importē 'datetime' bibleotēkas 'datetime' funkcijas, kas ļauj saglabāt šobrīdējo laiku un to formatēt.
from datetime import datetime

# Izveido funkciju 'save' ar 2 ievadiem, 'timestamp', kas pieņem string mainīgo laika posma saglabāšanai, kā arī 'info', kas pieņem sarakstu .csv faila izveidei un saglabāšanai.
def save(info):
    
    # Izmantojot 'datetime' bibleotēku izveido string mainīgo, kurā saglabāts šobrīdējais datums un laiks faila nosaukumam. 
    current_timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    
    # Izveido faila nosaukuma mainīgo ar ievadīto datumu un laiku.
    file_name =  (f"{current_timestamp}.csv")

    # Izveido faila lokācijas mainīgo.
    file_path = path.join(path.dirname(__file__), '..', 'results', file_name)

    # Izveido faila lokācijas mainīgo.
    makedirs(path.dirname(file_path), exist_ok=True)

    # Atver failu ar nosaukumu 'file_name' un tajā ieraksta visu kas ir 'info' objektā.
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer_instance = writer(file)
        writer_instance.writerows(info)

    # Izdrukā konsolē paziņojumu par saglabātajiem rezultātiem un kur tie ir saglabāti.
    print(f"Dati tika saglabāti šajā lokācijā: {file_path}")

# Definē funkciju 'start_results', kas pievieno datiem sākuma informāciju kā laiku, versiju un galveni vieglākai datu nolasīšanai.
def start_results(repeated, user_query, mode):
    
    # Definē 'data' sarakstu, ar sākuma datiem un formatēšanu.
    data = [
        # Ievada šobrīdējo datumu, laiku un saglabā 'repeated' mainīgo.
        ["Datums","Laiks", "Atkārtotas reizes", "Python versija"]]
    
    # Ja atvērts tieši, šis skripts izpildīs main() funckiju.
    if __name__ == "__main__":
        data.append([datetime.now().strftime('%d-%m-%Y'),datetime.now().strftime('%H:%M:%S'),repeated,version.py_version])
    else:
        data.append([datetime.now().strftime('%d-%m-%Y'),datetime.now().strftime('%H:%M:%S'),repeated,subscripts.version.py_version])
    
    # Pieraksta ievadīto meklēšanas škirkli un datubāzes veidu.
    if mode == 'vector':
        data.append(["Ievada šķirklis", "Datubāzes veids"])
        data.append([user_query, 'Vektoru datubāze'])
    else:
        data.append(["Ievada šķirklis", "Datubāzes veids"])
        data.append([user_query, 'Relāciju datubāze'])
    data.append(["Atkārtojuma nr.p.k.", "Laiks (ms)", "Izvada ID", "Izvada nosaukums", "Izvada autors"])
    
    # Izvada pabeigto sarakstu 'data'.
    return data

# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():
    
    # Izveido rezultātu saraksta iesākumu
    data = start_results(10,'test_input','vector')
    
    # Saglabā iesākumu jaunā failā.
    save(data)

# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    
    # Importē 'version.py' failu, kas izveido mainīgo py_version ar šobrīdējo Python versiju.
    import version
    
    main()
    
# Ja atvērts netieši, šis skripts importēs ārēji 'version' faila mainīgo.
else:
    
    # Importē 'version.py' failu, kas izveido mainīgo py_version ar šobrīdējo Python versiju.
    import subscripts.version
