dayType = 2

weekend = 1
workday = 2
holiday = 3

if dayType == 1:
    pass

elif dayType == 2:
    pass

else:
    pass # poleenie nic nei robi nie przerywa petli itd ale nadaje sie aby wlozyc je tam gdzie cos bedzie trzeba jeszcze uzupelnic zostawia nam miejsce do wykrozystania
# skladnia uproszczona

dayDescription = 'weeknd' if dayType ==1 else '?'
print(dayDescription)
# lub zagniezdzone
dayDescription = 'weeknd' if dayType ==1 else 'workday' if dayType ==2 else 'holiday' # wyswietli workday jezeli daytape = 2
print(dayDescription)
# lab
price = 123
bonus = 23
bonus_granted = False

if bonus_granted:
    price -= bonus
print(price)
bonus = print('cena po znizce',price - bonus) if bonus_granted else print('brak znizki')

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
value = 'very good' if rating ==5 else  'good' if rating ==4 else 'weak'




