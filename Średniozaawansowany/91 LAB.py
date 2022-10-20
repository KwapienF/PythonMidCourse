class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []


    def __init__(self, name,kind,taste,additives, filling,GlutenFree):
        self.name = name
        if self.known_kinds.count(kind) == 0:
            self.kind = 'other'
        else:
            self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        Cake.bakery_offer.append(self)
        self.__GlutenFree = GlutenFree

    def show_info(self):
        print(self.name.upper(),self.taste)
        if self.additives:
            print(self.additives)
        else:
            print('There are no additives')
        if self.filling:
            print(self.filling)
        else:
            print('There are any filling')
        print('GlutenFree:     ',self.__GlutenFree)
    def set_fillig(self,add_filling):
        self.filling += add_filling
        print('Dodano {}, nadzienie skłąda się z {}'.format(add_filling,self.filling))


    def set_additives(self,add_additives):
        self.additives.append(add_additives)
        print('Dodano {}, dodatki składają się z {}'.format(add_additives,self.additives))




cake1 = Cake('Tort urodzinowy', 'Tort', 'Berry',['fruits', 'toffi','jelly'],'Toffi with jelly, creamy',False)
cake2 = Cake('Brownie', 'muff', 'Cacao',['Jam', 'chocoloate'],'',False)
cake3 = Cake('Deans Pie', 'Pie', 'apple',[],'apples confiture',True)
cake4 = Cake('Cacao Waf', 'Waffel', 'nutella',[],'',True)


print('--'*30)
print(cake1.show_info())
print(cake2.show_info())
print(cake3.show_info())
print(cake4.show_info())

cake4.__GlutenFree = False

print(cake4.show_info())
print(dir(cake4))

cake4._Cake__GlutenFree = False # teraz udalo mi sie zmienic
print(cake4.show_info())

x = 1000
y = 0.03 * x
for i in range(5):
    x +=  y
    print(x)

print('Wartość końcowa inwestycji wynosi: {} PLN'.format(x))
