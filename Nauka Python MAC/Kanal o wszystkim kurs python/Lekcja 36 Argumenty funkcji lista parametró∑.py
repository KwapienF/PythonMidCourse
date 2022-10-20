def funkcja(arg1, arg2 = "World", *args, **kwargs): # tworzenie nieskonczonej lisy argumentow symbolem * w jednym args znajduja sie wszystkie inne argumenty ktore nie sa zadeklarowane
    #**kwargs  to argumenty ktorym mozna nadac etykiete {} slownik a *args da nam krotke()
    print(arg1, arg2, args, len(args), kwargs) # wpisalismy args tylko a wyprintuje kilka argumentow jaks ie wpisze jak nizej
    for x in args:
        print(x) # wyswietli wszystkie argumenty jakei dodamy w *arg
    for x in kwargs.values(): # values czyli chcemy iterowac po samych wartosciach a nie po kluczu i wyswietli tylko sebastian i 2022
        print(x)
    for x in kwargs.keys(): # po kluczach wyswietlimy autor i rok
        print(x)
funkcja("Hi", "Youtube")
funkcja("Hi", "Youtube", "!", " :)", autor="Sebastian", rok=2022) # wpisalismy dodatkowe dwa argumenty ktore weszly pod *args i zostaly wyswietlone
# przy wywolaniu *args otrzymujemy krotke
# autor to klucz sebastian to wartosc  rok to klucz 2022 to wartosc

