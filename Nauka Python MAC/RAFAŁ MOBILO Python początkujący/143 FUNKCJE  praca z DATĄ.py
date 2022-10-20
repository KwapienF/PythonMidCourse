import datetime
def data():
    now = datetime.datetime.now().strftime('%A')
    daynumber = datetime.datetime.now().strftime('%w') # numer dnia tygodnia i tutaj liczymy niedziele jako dzien zerowy!!!!!!
    print('Today is ',now)
    if int(daynumber) in (1,5):
        print('Mamy dzień roboczy')
    elif int(daynumber) in (6,7):
        delta = int(daynumber) - 5
        print('Za ',delta,' dni do pracy')
    return
data()

# sposób Mobilo dziala z datami
def GiveWorkingDay():
    day = datetime.date.today()
    if day.weekday() == 5:
        workingday = day + datetime.timedelta(days=2) # timedelta pozwala nam dodac do dat 2 dni
    elif day.weekday() == 6:
        workingday = day + datetime.timedelta(days=1)
    else:
        workingday = day
    print('Working day for ',day,' is ',workingday)
    return
GiveWorkingDay()



