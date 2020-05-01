#!/usr/bin/python
import os
from stat import *


def du_bs(rep = '.'):
    inodes = set()
    sum = 0
    for dirpath, subdirs, files in os.walk(rep):
        for fname in files:
            
            fpath = os.path.join(dirpath, fname)
            fstat = os.stat(fpath)
            
            if S_ISREG(fstat.st_mode):
                # print(fpath)
                # print("\t%s" % os.stat(fpath).st_size)
                if fstat.st_ino not in inodes:
                    print("file:", fname, "of size:", fstat.st_size)
                    sum += fstat.st_size
                    # print(fstat.st_ino)
                    inodes.add(fstat.st_ino)

    return sum


### Professor's provided solution... to a seemingly different exercise?
def prof_vers(rep = '.'):
    sum = 0
    for dirpath, subdirs, files in os.walk(rep):
        for fname in subdirs + files:
            sum += os.stat(os.path.join(dirpath, fname)).st_size

    return sum


if __name__== "__main__":
    print("total size: %s" % du_bs())

    # print(prof_vers())
