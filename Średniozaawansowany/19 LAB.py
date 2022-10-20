import os
import urllib.request

data_dir = r'c\:temp\lab19'
pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ] # lista slownikow
a = pages[0]
# print(a)
# print(a['name'])
for www in pages:
    try:
        path = r'{}'.format(os.path.join(data_dir,www['name']))
        open(path,'w+')
        urllib.request.urlretrieve(www['url'], path)
    except:
        print("Coś poszło nie tak")
        break
else:
    print("All pages downloaded successfully!!!")



