class Cake:
    def __init__(self, name,kind,taste,additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake1 = Cake('Tort urodzinowy', 'Tort', 'Berry',['fruits', 'toffi','jelly'],'Toffi with jelly, creamy')
cake2 = Cake('Brownie', 'muff', 'Cacao',['Jam', 'chocoloate'],'')
cake3 = Cake('Deans Pie', 'Pie', 'apple',[],'apples confiture')

bakery_offer = [cake1,cake2,cake3]
print('Todays offer:')
for product in bakery_offer:
    print(('\033[1m' + product.name) + '\033[0m',product.kind,'\033[1m'+product.taste+'\033[0m',product.additives,product.filling) # '\033[1m' pogrubienie i trzeba wskazac moment gdzie nei bedzie juz pogrubienia


