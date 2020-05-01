#!/usr/bin/python
import ex4
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_tree", metavar="F", type=str, nargs ='+',
                         help="file tree")
    # parser.add_argument("", action="store",dest="tree",help="File tree")
    parser.add_argument("-n", "--name", action="store", dest="name",
                        help="Find files with given name")
    parser.add_argument("-s", "--size", action="store", dest="size",
                        help="Find files of given size")
    parser.add_argument("-c", "--clean", action="store_true", dest="remove",
                        help="Remove matching files")

    return parser.parse_args()


if __name__== "__main__":
    options = get_args()
    if options.remove and not (options.name or options.size):
        exit("ERROR, must specify which files to remove")


## WHAT TO DO ABOUT THE FILE TREE PASSED BEFORE ANY OF THE FLAGS??
    tree = sys.argv[1]

    if options.name:
        if not options.remove:
            ex4.find_nom(options.name, tree)
        else:
            ex4.find_nom(options.name, tree, True)
    elif options.size:
        if not options.remove:
            ex4.find_taille(options.size, tree)
        else:
            ex4.find_taille(options.size, tree, True)
    

