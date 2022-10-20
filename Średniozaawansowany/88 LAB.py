class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []


    def __init__(self, name,kind,taste,additives, filling):
        self.name = name
        if self.known_kinds.count(kind) == 0:
            self.kind = 'other'
        else:
            self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        Cake.bakery_offer.append(self)

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
    def set_fillig(self,add_filling):
        self.filling += add_filling
        print('Dodano {}, nadzienie skłąda się z {}'.format(add_filling,self.filling))


    def set_additives(self,add_additives):
        self.additives.append(add_additives)
        print('Dodano {}, dodatki składają się z {}'.format(add_additives,self.additives))




cake1 = Cake('Tort urodzinowy', 'Tort', 'Berry',['fruits', 'toffi','jelly'],'Toffi with jelly, creamy')
cake2 = Cake('Brownie', 'muff', 'Cacao',['Jam', 'chocoloate'],'')
cake3 = Cake('Deans Pie', 'Pie', 'apple',[],'apples confiture')
cake4 = Cake('Cacao Waf', 'Waffel', 'nutella',[],'')


print('--'*30)
print(cake1.show_info())
print(cake2.show_info())
print(cake3.show_info())
print('--'*30)
print(cake1.set_fillig('MUSTARD?!? '))
print('--'*30)
print(cake1.set_additives('Ketchup '))
print('--'*30)
print(cake4.kind)
print(cake1.bakery_offer)
print('--'*30)
for c in Cake.bakery_offer:
    c.show_info()

print(isinstance(cake1,Cake))
print(type(cake1))
print(vars(Cake))
print(dir(Cake))
