#!/usr/bin/env python3

###############################################################################
# Implementation of `tree` command in python
###############################################################################

from os import getcwd, listdir
from os.path import isdir, isfile, join
from sys import argv
from time import sleep

delay = 0.05

amount_dirs = 0
amount_files = 0


def treep(directory, indent=""):
    files = listdir(directory)
    files.sort()

    for i, file in enumerate(files):
        path = join(directory, file)
        is_last = i == len(files) - 1
        if isfile(path):
            global amount_files
            amount_files += 1
            print(indent + "└── " + file if is_last else indent + "├── " + file)
            sleep(delay)
        elif isdir(path):
            global amount_dirs
            amount_dirs += 1
            print(indent + "└── " + file if is_last else indent + "├── " + file)
            sleep(delay)
            new_indent = indent + "    " if is_last else indent + "│    "
            treep(path, new_indent)


def main():
    if len(argv) > 2:
        print("Error: too many arguments")
        exit(1)
    if len(argv) == 1:
        path = getcwd()
        print(".")
    else:
        path = argv[1]
        print(path)
    treep(path)
    print(f"{amount_dirs} directories, {amount_files} files")


if __name__ == "__main__":
    main()
