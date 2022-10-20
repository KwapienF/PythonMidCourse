persons = ['Elisa','Steven@sales.mycompany.com', 'Filip', 'Marta@mycompany.eu', 'Raphael']
domain = 'mycompany.com'
email = []
email2 = []

for person in persons:
    if '@' in person:
        email.append(person)
    else:
        email.append(person + '@' + domain)

print(email)

# to samo z continue
for person in persons:
    if '@' in person:
        email2.append(person)
        continue
    email2.append(person + '@' + domain)
print(email2)

