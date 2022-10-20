import datetime

def sylwester():
    today = datetime.datetime.now()
    #print(today)
    year1 = datetime.datetime.now().strftime('%Y')

    #print(year1)
    endofyear = datetime.datetime(int(year1), 12,31)
    #print(endofyear)
    delta = endofyear-today
    print('End of the year is for',delta)
    return
sylwester()


def DaysToEndOfYear():
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)


DaysToEndOfYear()