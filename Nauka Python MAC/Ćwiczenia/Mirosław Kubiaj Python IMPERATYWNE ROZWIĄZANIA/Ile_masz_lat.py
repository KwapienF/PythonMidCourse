import datetime
i = datetime.date.today()
b = i.timetuple()
# now = datetime.datetime.now()
# print(now.strftime("%A"))

#"Program"
imie = input("Hej! Jak masz na imię?: ")
print(f"Witaj {imie}!")
if imie[-1] == "a":
    o1 = int(input("W jakim roku się urodziłaś: "))
    o2 = int(input("Którego miesiąca się urodziłaś? Podaj jako liczbę 1-12: "))
    o3 = int(input("Którego dnia?: "))
    imieona = datetime.date(o1,o2,o3)
    imieona1 = imieona.timetuple()
    imieona3 = imieona1.tm_wday
    imieona4 = imieona1.tm_year
    if imieona3 == 0:
        print("Urodziłaś się w poniedziałek")
    elif imieona3 == 1:
        print("Urodziłaś się we wtorek")
    elif imieona3 == 2:
        print("Urodziłaś się w środę")
    elif imieona3 == 3:
        print("Urodziłaś się w czwartek")
    elif imieona3 == 4:
        print("Urodziłaś się w piątek")
    elif imieona3 == 5:
        print("Urodziłaś się w sobotę")
    else:
        print("Urodziłaś się w niedzielę")
    print(f"Masz {b.tm_year - imieona4-1} lat")
else:
    m1 = int(input("W jakim roku się urodziłeś: "))
    m2 = int(input("Którego miesiąca się urodziłeś? Podaj jako liczbę 1-12: "))
    m3 = int(input("Którego dnia?: "))
    imieon = datetime.date(m1,m2,m3)
    imieon1 = imieon.timetuple()
    imieon3 = imieon1.tm_wday
    imieon4 = imieon1.tm_year
    if imieon3 == 0:
        print("Urodziłeś się w poniedziałek")
    elif imieon3 == 1:
        print("Urodziłeś się we wtorek")
    elif imieon3 == 2:
        print("Urodziłeś się w środę")
    elif imieon3 == 3:
        print("Urodziłeś się w czwartek")
    elif imieon3 == 4:
        print("Urodziłeś się w piątek")
    elif imieon3 == 5:
        print("Urodziłeś się w sobotę")
    else:
        print("Urodziłeś się w  niedzielę")
    print(f"Masz {b.tm_year - imieon4 -1} lat")
print("KONIEC :)")








