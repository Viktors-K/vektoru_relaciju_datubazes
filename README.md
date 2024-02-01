
# VEKTORDATUBĀZES UN KĀ TĀS PAĀTRINA MEKLĒŠANU DATU KOPĀS: Praktiskā daļa

Zinātniskās pētniecības darbs inženierzinātņu un tehnoloģiju nozarē.

Šajā projektā ir divi galvenās programmas: main_vector.py un main_relational.py. Šīs programmas ļauj mērīt vidējo laiku meklēšanas pieprasījumam dažādās datubāzēs, attiecīgi vektoru datubāzēs un relāciju datubāzēs, no tiem pašiem sākuma datiem.

Projekta mērķis ir izpētīt cik ātras vektoru un relāciju datubāzes ir meklēšanas pieprasījumos.

## Kā izmantot šo projektu?

/data/ mapē tiek ievietots first.csv fails, kurā ir 5 kolonnas - ID, Title, Author, Date un Text. 


ID kolonnā tiek sarakstīti unikāli ID katrai rindai, lai rezultātus varētu atšķirt. 

Title kolonnā tiek pievienots kāda raksta nosaukums, kuru izmantos gan meklēšanai, gan rezultātu dekodēšanai. 

Author un Date kolonnās tiek attiecīgi pierakstīti raksta autors un datums, šie dati ir metadati, kuri netiks izmantoti meklēšanai, bet atkal, rezultātu dekodēšanai. 

Pēdējā kolonnā, Text, tiek pievienots raksta teksts, vai daļa no tā, šī informācija būs galvenais datu avots meklēšanai.

###

Pēc sākotnējo datu izveides, tiek palaista main_vector.py vai main_relational.py programma, atšķirībā no kuru datubāzi vēlas izmantot, attiecīgi vektoru datubāzi vai relāciju datubāzi.

Pēc palaišanas, konsolē tiek jautāts cik reizes atkārtot laika mērīšanu datu precizēšanai. Pēc skaitliska ievada, tiek jautāts ievada šķirklis, ko izmantot meklēšanai datubāzē. 

Kad mērīšana ir pabeigta, konsolē būs paziņojums, ka dati tika saglabāti .csv failā šobrīdējās direktorijas /results/ mapē, kas tiks izveidota, ja tā neeksistē. Faila nosaukums būs atbilstošs programmas palaišanas datumam un laikam. 

###

