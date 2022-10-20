netto = 1230
brutto = 1223
def Funkcja1(netto,brutto):
    if netto > brutto:
        raise Exception('Netto cant be higher than brutto!')
    else:
        print(f'netto: {netto}, brutto: {brutto}')

try:
    Funkcja1(netto,brutto)
except ValueError as e:
    print('Wrong Value')
    raise ValueError('Something wrong with value') from e
except Exception as e:
    print(e)
    raise ValueError('Something wrong with value') from e


