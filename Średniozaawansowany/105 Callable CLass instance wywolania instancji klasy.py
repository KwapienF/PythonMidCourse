class MemoryClass:
    def __init__(self,list):
        self.list_of_itmes = list
   #nie robimy tak tylko inna metodą ponizej
    # def add_item(self,item):
    #     self.item = item
    #     self.list_of_itmes.append(self.item)
    def __call__(self, item): # predefiniwoana funkcja ktora powoduje ze bedzie mozna wywolywac instancje klasy tak jakby byly one funkcjami czyli beda callable
        self.list_of_itmes.append(item)
mem = MemoryClass([]) #  tworzy powstanie instancji o nazwie mem ktora w zmiennej listofitems bedzie przechowywac pusta liste
print('List of items in memory: ',mem.list_of_itmes)
mem.list_of_itmes.append('Sugar')
print('List of items in memory: ',mem.list_of_itmes)
print(callable(MemoryClass)) # czy mozna w tej chwili je wywolywac  tu mozna
print(callable(mem)) # nie jest bo nie jest funkcja

# dzieki call teraz tylko przekazujemy do mem argmenty aby cos dodac do listy
mem('Fruits')
print('List of items in memory: ',mem.list_of_itmes)


