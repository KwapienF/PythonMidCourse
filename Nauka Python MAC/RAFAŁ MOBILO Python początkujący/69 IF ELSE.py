age = int(input('Podaj wiek: '))
isDrunk = input('Czy jest pijany? tak lub nie: ')
if isDrunk == 'tak':
    isDrunk = True
    b = 'Klient jest pijany.'
    if age >= 18:
        a = 'Wiek zaakceptowano'
        print(a, b, ' i nie można sprzedać alkoholu')
    else:
        a = 'Klient nie ma 18 lat'
        print(a,b,' i nie można sprzedać alkoholu')
elif isDrunk == 'nie':
    isDrunk = False
    b = 'Klient jest trzeźwy.'
    if age >= 18:
        a = 'Wiek zaakceptowano'
        print(a, b, ', więc można sprzedać alkohol')
    else:
        a = 'Klient nie ma 18 lat'
        print(a, b, ' i nie można sprzedać alkoholu')







