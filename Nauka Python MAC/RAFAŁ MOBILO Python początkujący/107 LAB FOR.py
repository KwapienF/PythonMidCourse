text = '''ndustrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''
list = text.replace('\n',' ').split(' ')

print(list)
pword = 0
for word in list:
    if 'p' in word.lower():
        pword += 1

print(pword)

# zad 3
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
key = dictionary.keys()
print(key)

for key in dictionary:
    i = 0
    a = (dictionary[key[i]])
    print(key[i], '-',a)
    i += 1

# zad 3 krócej <faceplam to co wyżej
for word in dictionary.keys():
    print(word,'-',dictionary[word])