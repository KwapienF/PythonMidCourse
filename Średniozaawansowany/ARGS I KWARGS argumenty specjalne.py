def BuyMe(prefix = 'Im begging You',what = 'something nice',*args, **kwargs): # args pozwala na dodanie ilu sie chce argumnetow moze sie nazywac inaczej nie koniecznie args byle miala gwiazdke przed sobą
    print(prefix,what)
    print(args)
# kwargs to argument poprzedzony nazwą czyli key word arg kwarg :)
    print(kwargs) # kwrgs tworzy slownik
BuyMe("prosze",'Kup mi cos','a dog','a candy', shop = 'Market', color = 'any') # arg utworzy tuple kwarg slownik
# jak wywoalc taka funkcje gdzie mamy juz liste zakupow?
products = ['milk', 'juice','coke']
parameters = {'price':'low', 'time':'now'}
BuyMe('Buy me', 'newspaper',products,parameters) # args utworzy tuplet dwuelementowy skladajacy sie z listy i slownika nie o to nam chodziło
BuyMe('Buy me', 'newspaper',*products,**parameters) # stworzy oddzielnie tuplet i slownik a nie polaczy to w tuple dwuelementowy

# LAB
def calculate_paint(efficency_Itr_per_m2,*powierzchnia):
    for i in range(len(powierzchnia)):
        print(f'You need {float(efficency_Itr_per_m2) * float(powierzchnia[i])} liters of paint')
calculate_paint(2,20,40)
rooms = [10,20,30,23.3]
calculate_paint(0.3,*rooms)

# lab 2
def log_it(*args):
    plik = open(r'c:\temp\log_it.txt', 'w')
    for i in args:
        plik.write(f'{i} ')
    plik.close()
log_it('Filip','kochać', 'Leciunie')












