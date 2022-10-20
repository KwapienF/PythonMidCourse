# funkcji switchi case nie ma w pythonie ale mozna ja zasymukowac
# w innych jezykach wyglada to tak:
# function(argument){
#     switch(argument) {
#         case 0:
#             return "lundi"
#         case 1:
#             return "mardi"
#         case 2:
#             return "mercredi"
#         case 3:
#             return "jeudii"
#         case 4:
#             return "vendredi"
#         case 5:
#             return "samedi"
#         case 6:
#             return "dimanche"
#         default:
#             return "! error !"
#     };
# };

# jak zrobic w pythonie

def WeekdDayFrench(daynumber):
    names = {
        0: "lundi",
        1: "mardi"
    }
    return names.get(daynumber, "error") # metoda get ma wybrac z slownika names daynumber a jak niebedzie elementu to wyswietli error
print(WeekdDayFrench(1))

# czyli robimy funkcje i okreslamy paramter ktory jest casem i w srodku funckji odwolujemy sie metodą get do tego parametru by wybrala ze slownika odpowiednie wartosci nie trzeba tutaj awiasow kwadratowych

