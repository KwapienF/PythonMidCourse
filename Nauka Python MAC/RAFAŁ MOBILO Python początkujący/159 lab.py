def Print(*a):
    for i in a:
        if i == 'cat':
            # this function prints a cat ascii-art
            txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
            print(txt)




        elif i == 'bear':
            # this function prints a bear ascii-art
            txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
            print(txt)


        elif i == 'bat':
            # this function prints a bat ascii-art
            txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/  
         '''
            print(txt)



Print('bat','bear','cat')



from datetime import date
def DaysToEndOfYear(*dates):

    for date_today in dates:
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print(delta.days)


DaysToEndOfYear(date(2022,4,22))
