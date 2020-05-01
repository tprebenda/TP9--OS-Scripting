#!/usr/bin/python
import os
import sys
import subprocess




if __name__== "__main__":
    if len(sys.argv) < 3:
        sys.exit("Command should be of form: <script> <file_tree> <mod_code>")
    f_tree = sys.argv[1]
    code = sys.argv[2]       # Can this be a string?

    for dirpath, subdirs, files in os.walk(f_tree, topdown=False):
        for fname in files:
            f_path = os.path.join(dirpath, fname)
            os.chmod(f_path, int(code))
            # subprocess.call(['chmod', code, f_path])    // Alternative method

