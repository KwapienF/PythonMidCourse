import datetime
import functools
#logfilepath = r'c:\temp\functionlog.txt' nie jest potrzebne bo przekazemy ja do wrapera z apomocą parametru
# musimy dac wrapera w srodek kolejnej funkcji ktora przekaze z dekoratora sciezke pliku
def CreateFunctionWithWrapper_LogToFile(logfilepath): # przyjmuej sciezke do pliku
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args,**kwargs):
            file = open(logfilepath,'a') # a oznacza ze jesli plik istniejej to nalezy do niego dopisywac dane nie zastepwoac na nowo
            file.write('-'*20 + '\n')
            file.write(f'Function {func.__name__} started at {datetime.datetime.now()}')  # funkcja.__name__ wyswietli nazwe funkcji
            file.write('Following arguments were used:\n')
            file.write(" ".join("{}".format(x) for x in args)) # parametr jest listą a my chcemy dodac napsi dlatego dla pistego napisju spacji dodajemy(join) napis parametru
            file.write('\n')
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items())) # ta sama sztuczka co wyzej w args k key v value for (k,v) in kwargs.items oznacza wartosci znajdujace sie w tablicy
            file.write('\n')
            result = func(*args,**kwargs)
            file.write(f'Function returned {result} ')
            file.write('\n')
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile(r'c:\temp\changeSalary.txt') # wraper zapsiuajcy do pliku gdy chodzi i zmiane pensji
def ChangeSalary(emp_name, newsalary, is_bonus = False):
     print('Changing Salary for {} to {} as bonus={}'.format(emp_name,newsalary,is_bonus))
     return newsalary

@CreateFunctionWithWrapper_LogToFile(r'c:\temp\changeposition.txt') # wraper zapsiuajcy do pliku gdy chodzi i zmiane stanowiskai
def Changeposition(emp_name, newposition, is_bonus = False):
     print('Changing position for {} to {} as bonus={}'.format(emp_name,newposition,is_bonus))
     return newposition

print(ChangeSalary('John', 14000, True))
print(ChangeSalary('Mike', 15000, is_bonus = True))

print(Changeposition('Michae', 'Salesman'))
print(Changeposition('Anke', 'Manager'))