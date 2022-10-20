import os
# grep  ma wyszukac w systemie operacyjnym nazwy plikow ktreo zawieraja okreslony ciag znakow

path = r'C:\temp'  # ścieżka w ktorej nalzwy wyszukiwac pliki
search_string = 'Ford'
file_extension = '.py'

for dir_name, subdirs, filenames in os.walk(path): # katalogi podkatalogi i nazwy polikow
    #print(dir_name,subdirs,filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
            fullfileName = os.path.join(dir_name,filename)
            for line in open(fullfileName):
                if search_string in line:
                    print(filename)

def generate_files(base_dir,file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullfileName = os.path.join(dir_name, filename)
                yield fullfileName

def grep_files(search_string,files):
    for file in files:
        with open(file) as text:
            if search_string in text.read():
                yield file

file_generator = generate_files(path,file_extension)
for file in grep_files(search_string,file_generator): # przekazujemy generator do generatora  robimy funckje ktora jako argument przyjmuje generator
    print(file)

