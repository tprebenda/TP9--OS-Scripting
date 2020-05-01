#!/usr/bin/python
import os
import re

def find_nom(exp, rep = '.', rem = False):
    filtre = re.compile(exp)
    for dirpath, subdirs, files in os.walk(rep):
        for fname in files:
            if filtre.search(fname.lower()):       
                relpath = os.path.join(dirpath, fname)
                if not rem:
                    print(os.path.join(os.getcwd(), relpath))
                else:
                    print("file deleted:", relpath)
                    os.remove(os.path.join(relpath))



def find_taille(tail, rep = '.', rem = False):
    for dirpath, subdirs, files in os.walk(rep):
        for fname in files:
            # print(dirpath)
            fpath = os.path.join(dirpath, fname)
            fstat = os.stat(fpath)
            if fstat.st_size == tail:
                if not rem:
                    print(os.path.join(os.getcwd(), fpath))
                else:
                    print("file deleted:", fname)
                    os.remove(os.path.join(dirpath, fname))


if __name__== "__main__":
    # find_nom(r".*\.jpe?g", "Arbo")

    find_taille(74)      # Prints a '.' in the full path (comes from dirpath)





