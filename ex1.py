#!/usr/bin/python
import os
import re

def list_jpeg(rep = '.'):
    l = []
    for dirName, subdirs, files in os.walk(rep):
        # print("Searching directory: %s" % dirName)
        for f in files:
            # print(f)
            if re.search(r".*\.jpe?g", f.lower()):
                # print("\tmatch:", f)
                l.append(f)

    return l


def list_jpeg_r(rep = '.'):
    l = []
    for dirName, subdirs, files in os.walk(rep):
        # print("Searching directory: %s" % dirName)
        for f in files:
            if re.search(r".*\.jpe?g", f.lower()):
                path = os.path.join(os.getcwd(), dirName)
                l.append(os.path.join(path, f))

    return l


def range_jpeg(dir_out, rep = '.'):
    if not os.path.isdir(dir_out):
        os.mkdir(dir_out)

    ####### OR...
    # try:
    #     os.mkdir(rep, 0o755)
    # except FileExistsError:
    #     print("Directory already exists")
        
    jpegs = list_jpeg_r(rep)
    for path in jpegs:
        (ref, name) = os.path.split(path)
        dst = os.path.join(dir_out, name.lower())
        os.link(path, dst)

       



        

        


if __name__== "__main__":
    jpegs = list_jpeg()
    # print(jpegs)
    # print(len(jpegs)) # Should be 18

    jpeg_paths = list_jpeg_r("Arbo")
    print(jpeg_paths)
    # print(len(jpeg_paths))

    # range_jpeg("test")



