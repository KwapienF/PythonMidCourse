import os
import requests

def gen_get_files(dir):
    for i in os.listdir(dir):
        yield os.path.join(dir,i)

def gen_get_file_lines(filename):
    with open(filename, 'r') as text:
        for line in text.readlines():
            yield line.replace('\n', '') # zwracacj linijke textu znak eneter zastepujemy niczym aby bylo w jednym zdaniu

def check_webpage(url):
    try:
        url_site = requests.get(url)
        return url_site.status_code == 200
    except:
        return False


try:
    os.mkdir('c:/temp/links_to_check')
except:
    pass

with open('c:/temp/links_to_check/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('c:/temp/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files(r'c:/temp/links_to_check'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))
