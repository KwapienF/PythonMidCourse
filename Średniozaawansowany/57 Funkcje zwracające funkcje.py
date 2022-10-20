def Calculate(kind='+',*args):
    result = 0
    if kind == '+':
        for a in args:
            result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result

print(Calculate('-',20,9,8,4))

# inny sposob pythonowski

def Create_function(kind = '+'):
    source = '''  
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
'''.format(kind)
    exec(source, globals())# wywolujemy srodowisko globals bo inaczej excec nie zwroci wyniku excec musi miec dostep do biezacego srodowiska
    return f
# create fucntion zwroiclo nam funckje ktora ponizej teraz zapaietujemy w zmiennej
f_add = Create_function('+') # funkcja dodająca
print(f_add(1,2,3,4))
#LAB
print('LAB ' * 40)

import datetime
def Newf(kind = 'minutes'):
    def sub(first,second):
        if kind == 'minutes':
            date1 = datetime.date(first[0],first[1],first[2])
            date2 = datetime.date(second[0],second[1],second[2])
            result = date1 - date2
            return result.total_seconds()/60, 'minut'
        elif kind == 'hours':
            date1 = datetime.date(first[0], first[1], first[2])
            date2 = datetime.date(second[0], second[1], second[2])
            result = date1 - date2
            return result.total_seconds()/60/60, 'godzin'
        elif kind == 'days':
            date1 = datetime.date(first[0], first[1], first[2])
            date2 = datetime.date(second[0], second[1], second[2])
            result = date1 - date2
            return result.total_seconds()/60/60/24, 'dni'

    return sub

minutes = Newf('days')
print('Różnica wynosi: ', minutes((2022,4,5),(2021,4,5)))

# z uzyciem exec

def Newf2(kind = 'minutes'):
    if kind == 'minutes':
        x = 60, 'minuten'
    elif kind == 'hours':
        x = 3600, 'godzinen'
    elif kind == 'days':
        x = 60*60*24, 'dzionków'
    source = '''
def sub(first,second):
    date1 = datetime.date(first[0], first[1], first[2])
    date2 = datetime.date(second[0], second[1], second[2])
    result = date1 - date2
    return result.total_seconds()/{}, '{}'
        '''.format(x[0],x[1])
    exec(source,globals())
    return sub

execfunc = Newf2('hours')
print('Różnica wynosi: ', execfunc((2022,4,5),(2021,4,5)))



# date1 = datetime.date(2022,5,21)
# date2 = datetime.date(2022,4,2)
# result = date1 - date2
# print(result.total_seconds()/60) # roznica w minutach
#
# date1 = datetime.date(2022,5,21)
# date2 = datetime.date(2022,4,2)
# result = date1 - date2
# print(result.days * 24) # roznica w godzinach
#
# date1 = datetime.date(2022,5,21)
# date2 = datetime.date(2022,4,2)
# result = date1 - date2
# print(result.days) # roznica w dniach


# sposób mobilo

from datetime import datetime


def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]


def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]


def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))


def create_function(span):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''.format(sec)

    exec(source, globals())

    return f


f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))




















