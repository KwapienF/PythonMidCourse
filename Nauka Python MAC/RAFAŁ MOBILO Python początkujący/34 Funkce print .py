a = 'This is a text'
print(a.endswith('xt.'))
print(a.islower())
print(a.upper())
print(a.lower())
print(a.find('text'))
print('-----------------')
print(a.find('qq',11))  # ,5 oznacza ze szuka napisu od literki nr 5 w zdaniu. bo czasem si emoze powtarzac. liczy o d0 1 2 3 4 5 czyli od 6 znaku
a = a.replace('text', 'text'.upper())
print(a) # replace zamienia na znaki w teksice
print(a.replace('T', '4').replace('is','44')) # replace mozna laczyc w ciag
print(a.split(' ')) # powstanie tabela, dzieli na tekst na stale w tabeli oddzielone spacja lub znakiem
b = '1000'
print(b.isdigit()) # sprawdza czy tekst wyglada jak liczba
print(b.isdecimal()) # sprawdza czy tekst wyglada jak liczba ktora moze meic wartosci po przecinku
print(b.isalpha()) # sprawdza czy tekst wyglada jak literki
print(b.isalnum()) # sprawdza czy tekst wyglada jak alnum alpha numeryczny czyli czy ma literki i cyferki lub to i to
b = int(b) # konwertuje tekst na liczbe jezeli sie da czyli isdigit or decimal must gave TRUE
print(b + 1)
print('------------------', '\n')
# LAB
q = ('A good programmer is someone who always looks both ways before crossing a one-way street')
print(q.upper())
print(q.lower())
print(q.endswith('street'))
print(q.isupper())
print(q.upper().isupper())
print(q.find('one'))
print(q.replace('one', '1').replace('both', '2'))
print(q.split(' '))
