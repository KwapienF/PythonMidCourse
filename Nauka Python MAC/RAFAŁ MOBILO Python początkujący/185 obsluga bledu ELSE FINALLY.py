import sys
taskperperson = 0

try: # sprobouje wykonac
    tasks = 32
    personStr = input('Ile osob ma druzyna?')
    persons = int(personStr)

    taskperperson = tasks / persons
except ValueError as e:
    print('bład wartosci',e)
except ZeroDivisionError as e:
    print('musi byc liczba wieksza od 0',e)


except: # jesli dojdzie do bledu to wykona sie to co  w except, jak sa wyzej inne excepct to ta zadziala na bledy ktore nie sa uwzglednione wyzej
    print('something went wrong', sys.exc_info()[0]) # sys exc info zwraca blad  w postaci tuple z 3 elemetnow ale pierwsyz jest najwazneijszt stad dalismy aby tylko go pokazal [0]
else: # jak tu uzyjemy else to to zadziala wtedy jak nie bedzie bledu a nie zawsze pomimo ze jakis blad bedzie
    print('kazdy ma', taskperperson, 'zadan')
finally: # instrukcja finally wykona sie niezaleznie od tego czy doszlo do bledu czy nie, zawsze sie wykona
    print('koniec programu')