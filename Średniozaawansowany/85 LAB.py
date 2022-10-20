class Cake:
    def __init__(self, name,kind,taste,additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
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

bakery_offer = [cake1,cake2,cake3]
print('Todays offer:')
for product in bakery_offer:
    print(('\033[1m' + product.name) + '\033[0m',product.kind,'\033[1m'+product.taste+'\033[0m',product.additives,product.filling) # '\033[1m' pogrubienie i trzeba wskazac moment gdzie nei bedzie juz pogrubienia
print('--'*30)
print(cake1.show_info())
print(cake2.show_info())
print(cake3.show_info())
print('--'*30)
print(cake1.set_fillig('MUSTARD?!? '))
print('--'*30)
print(cake1.set_additives('Ketchup '))


