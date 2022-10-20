
def GiveWorkingDay(year, month, day):
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
GiveWorkingDay(2022,4,23)
GiveWorkingDay(year=2022,month=4,day=23)
GiveWorkingDay(day=23, month=4,year=2022,) # przypisując do parametrow mozna zmienaic kolejnsoc

# lab
def Print(a = ''):
    if a == 'cat':
        # this function prints a cat ascii-art
        txt = r'''
|\---/|
| o_o |
 \_^_/'''
        print(txt)
        return



    elif a == 'bear':
        # this function prints a bear ascii-art
        txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
        print(txt)
        return
    elif a == '':
        print('nicniewpisałeś')
        return



    if a == 'bat':
        # this function prints a bat ascii-art
        txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
        print(txt)
        return


a = (input('Choose Cat, Bear or bat: '))
a = a.lower()
Print(a)

from datetime import date
def DaysToEndOfYear(year,month,day):
    from datetime import date
    date_today = date(year,month,day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

DaysToEndOfYear(2022,4,5)
