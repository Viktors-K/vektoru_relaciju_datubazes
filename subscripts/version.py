# Importē 'sys' bibleotēkas 'version_info' funkciju, kas ļauj pārbaudīt izmantoto Python versiju.
from sys import version_info

# Izveido mainīgo 'py_version', kas saglabā izmantoto Python versiju.
py_version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"

# Definē funkciju 'main', kas izpilda galvenās funkcijas šajā zemā līmeņa skriptā.
def main():
    
    # Izdrukā Python versijas informāciju.
    print("Version info.")
    print(py_version)

# Ja atvērts tieši, šis skripts izpildīs main() funckiju.
if __name__ == "__main__":
    main()
