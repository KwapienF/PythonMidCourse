class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def __str__(self):
        return f'Product: {self.kind} + {self.name}, additives: {self.additives}'
    def __iadd__(self, other):
        if type(other) is list:
            additives = self.additives
            additives.extend(other)
            return additives
        elif type(other) is str:
            additives = self.additives
            additives.append(other)
            return additives
        else:
            raise Exception('For adding more additives than 1 please add as a list')

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)
cake01 += ['KOLOROWE POSYPKI','SOSY']
print(cake01)
