import random
class MemoryClass:
    list_of_already_Selected_item = []
    def __init__(self,function):
        print('this is init of MemoryClass')
        self.function = function
    def __call__(self,list):
        print('this is call of MemoryClass')
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_Selected_item]
        print('Selecting only from a list of: ',items_not_selected)
        item = self.function(items_not_selected)
        MemoryClass.list_of_already_Selected_item.append(item)
        return item



cars = ['Opel','Fiat','Polonez','Porsche','Citroen','BMW','Volkswagen','Renault','Kia']
@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars) # randomowy choice...bruh
@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)
@MemoryClass
def SelectFreeAccesories(list_of_cars):
    return random.choice(list_of_cars)

print('Promotion: ',SelectTodayPromotion(cars))
print('Show: ',SelectTodayShow(cars))
print('Free Accesories: ',SelectFreeAccesories(cars))