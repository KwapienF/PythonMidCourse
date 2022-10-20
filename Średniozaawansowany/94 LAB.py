class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []



    def __init__(self, name,kind,taste,additives, filling,GlutenFree,text):
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
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            print('Cannot add TEXT')

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
        print('Text? ',self.__text)

    def set_fillig(self,add_filling):
        self.filling += add_filling
        print('Dodano {}, nadzienie skłąda się z {}'.format(add_filling,self.filling))


    def set_additives(self,add_additives):
        self.additives.append(add_additives)
        print('Dodano {}, dodatki składają się z {}'.format(add_additives,self.additives))

    def __get_text(self):
        return self.__text
    def __set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('Cannot add TEXT')
    TEXT = property(__get_text,__set_text,None,'Text on the Cake')




cake1 = Cake('Tort urodzinowy', 'cake', 'Berry',['fruits', 'toffi','jelly'],'Toffi with jelly, creamy',False,'HapPy BirThDay')
cake2 = Cake('Brownie', 'muff', 'Cacao',['Jam', 'chocoloate'],'',False,'')
cake3 = Cake('Deans Pie', 'Pie', 'apple',[],'apples confiture',True,'')
cake4 = Cake('Cacao Waf', 'Waffel', 'nutella',[],'',True,'')


print('--'*30)
print(cake1.show_info())
print(cake2.show_info())
print(cake3.show_info())
print(cake4.show_info())

cake1.TEXT = 'Happy meal!'
print(cake1.TEXT)
cake2.TEXT = 'Happy meal!'
print(cake2.TEXT)


