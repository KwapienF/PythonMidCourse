# Administrator systemu chciałby wiedzieć, ile plików i katalogów znajduje się w określonym katalogu. Słyszał, że da się to zrobić w Pythonie i w sumie ma racje...

import os
import itertools as it

def scantree(path):
    for object in os.scandir(path):
        if object.is_dir():
            yield object
            yield from scantree(object.path)
        else:
            yield object

listing = scantree('C:/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)

listing = scantree('C:/temp')
slisting = sorted(listing, key=lambda x: x.is_dir())

for czyfolder, element in it.groupby(slisting,key=lambda x: x.is_dir()):
    print('DIR' if czyfolder  else 'FILE', len(list(element)))


