# eval() pozwala pobrac od uzytkownika jakis napis ktory to bedzie fagmentem kodu i bedzie mozna go samodzielnie uruchomic w pythonie

var_x = 10
password = 'My super secret password'
source = 'password' # to jest kawalek programu
result = eval(source)
print(result) # pobral kod z source i policzyl jak program

print(globals()) # funkcja globals pozwoli sie odwoalc do wszystkich obeiktow i pokaze wszystkie zdefuniowane zmienne
 # w eval moze odniesc sie haker do passwor di wtedy wyswietli mu haslow daltego aby przed tym sie zabezpieczyc zdefinujemy globlas nowe z ktorego usuniemy wrazliwe dla ans zmienne

globals = globals().copy()
del globals['password'] # usuwamy z naszej kopi zmiennych password by nie mozna ylo go wydobyc
result2 = eval(source,globals) # jako drugi argument do eval zawsze podajemy wykaz zmiennych globalnych
print(result2) # i prosze haslo jest nie zdefiniowane i juz sie nie wyswietli

# za kazdym razem tworzenie kopii globalnej i usuwanie z niej wrazliwych danych jest meczace ic zasochlonne lepiej tworzyc globals jako puste