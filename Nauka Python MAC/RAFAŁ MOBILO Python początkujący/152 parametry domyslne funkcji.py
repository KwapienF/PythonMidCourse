def GiveWorkingDay(year, month, day=1): # dopisujemy jeden jako domyslna wartosc wtedy mozna funkcje wywolywac tylko rokiem i miesiacem i jak nie podamy dnia to wtedy przyjmie domyslnie 1
    import datetime
    #day = datetime.date.today()
    day = datetime.date(year,month,day)
    if day.weekday() == 5:
        workingday = day + datetime.timedelta(days=2) # timedelta pozwala nam dodac do dat 2 dni
    elif day.weekday() == 6:
        workingday = day + datetime.timedelta(days=1)
    else:
        workingday = day
    print('Working day for ',day,' is ',workingday)
    return
GiveWorkingDay(2017,9)

# funkcja ta sama ale dla zawsze niezacej daty
from datetime import date
from datetime import timedelta
def GiveWorkingDay2(year=date.today().year, month =date.today().month , day = date.today().day): # dopisujemy jeden jako domyslna wartosc wtedy mozna funkcje wywolywac tylko rokiem i miesiacem i jak nie podamy dnia to wtedy przyjmie domyslnie 1

    #day = datetime.date.today()
    day = date(year,month,day)
    if day.weekday() == 5:
        workingday = day + timedelta(days=2) # timedelta pozwala nam dodac do dat 2 dni
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    print('Working day for ',day,' is ',workingday)
    return
GiveWorkingDay2()

# zwracanie z funcki wartosc za zewnatrz

def GiveWorkingDay3(year=date.today().year, month =date.today().month , day = date.today().day): # dopisujemy jeden jako domyslna wartosc wtedy mozna funkcje wywolywac tylko rokiem i miesiacem i jak nie podamy dnia to wtedy przyjmie domyslnie 1

    #day = datetime.date.today()
    day = date(year,month,day)
    if day.weekday() == 5:
        workingday = day + timedelta(days=2) # timedelta pozwala nam dodac do dat 2 dni
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    return workingday

nextworkingday = GiveWorkingDay3()
print(nextworkingday,'zwrocilo na zewnatrz')
