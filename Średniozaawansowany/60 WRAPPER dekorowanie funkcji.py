 # wrapper pozwala sledic dzialanie innych funkcji obudowuje funkcje dodatkowa zewnetrzna funkcji ktora robi cos jeszce
import datetime
import functools # modyfikowanie funkcji

def CreateFunctionWithWrapper(func): # funckaj ta obudowuje dowolna funckje w ten spsob ze printuje cos przed i po  a w srodku zwraca result danej funckji args i wargs mamy aby funkcja przyjmowala wszystkie mozliwe argumenty
    def func_with_wrapper(*args,**kwargs):
        print(f'Function {func.__name__} started at {datetime.datetime.now()}')  # funkcja.__name__ wyswietli nazwe funkcji
        result = func(*args,**kwargs)
        print(f'Function returned {result} zł')
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper # dekorator
def ChangeSalary(emp_name, newsalary, is_bonus = False):
     print('Changing Salary for {} to {} as bonus={}'.format(emp_name,newsalary,is_bonus))
     return newsalary

#print(ChangeSalary('Filip',20000,True))



#ChangeSalary = CreateFunctionWithWrapper(ChangeSalary) # astepujemy funkcje stara  funkcja z wrapperem
print(ChangeSalary('John',15000,True))
# Change salary zostanie obudowana wrapperem bo wczesniej udekorowalismy ja dekoratorem  zawierajacym ten wrapper wiec zastosuje do niej wrapper shiiiit
