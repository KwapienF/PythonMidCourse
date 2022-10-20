import re

if re.match("^[A-Z]o.$", "Rok"): #match sprawdza czy 1 arg pasuje do 2 arg . po ko sprawdzi czy jest wyraz ko, któ®y kocnzy sie dowolnym znakiem
   # daszek oznacza ze musi sie rozpoczynac sie do tego wzor, a symbol $ znaczy ze na tym ma sie konczyc czyli ma zaczyna sie od ko i konczyc jednym znakiem
   # [Kk]  oznacza nam klase znakow czyli jezeli dopasowano chociaz jeden ze znakow podanych w nawiasach to  wywali True
   # Można zrobi przedzial znakow [A-Z]  i to oznacza wszystkie duze znaki alfabetu
   # mozna dopisac drugi rpzedzial malych liter ^[A-Za-z] pisze sie bez spacji bez niczego drugi przedzial od razu za pierwszym
   # mozemy zanegowac przedzial aby nie bylo tych znakow ^[^A-Za-z] symbolem daszku i wtdey dopasuje wszystkie znaki ktore nie nalezą do przedzialu np cyfra 0
# symbol poczatku ^ oraz konca $
    print("Dopasowano")
else:
    print("Nie dopasowano")

if re.match("^[rR]ok[-_=][0-9][0-9][0-9][0-9]$", "Rok-1989"):
    print("Dopasowano")
else:
    print("Nie dopasowano")