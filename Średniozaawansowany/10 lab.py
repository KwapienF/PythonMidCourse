options = ['load data', 'export data', 'analyze & predict']
choice = 'x'
# def DisplayOptions():
#     bool = True
#     while bool:
#         a = int(input('Wybierz ipcje od 1-3: '))
#         if a >0 and a <4:
#             print(options[a-1])
#             bool = False
#         else:
#             print('Podaj liczbę 1,2 lub 3!')
# DisplayOptions()

# def DisplayOptions():
#     a = input('Wybierz ipcje od 1-3: ')
#     return a
#
# while choice:
#     choice = DisplayOptions()
#     if choice:
#         try:
#             choice_num = int(choice)
#             print(options[choice_num-1])
#         except:
#             print('Nieprawidłowy  liczba ma byc 1 2 lub 3')
#
#     else:
#         print('Koniec programu')


def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i + 1, options[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
options = ['load data', 'export data', 'analyze & predict']

while choice:

    choice = DisplayOptions(options)

    # executed only if something was entered
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')

