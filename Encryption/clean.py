# Clean

import os

def cleanTemp(*argv):
    for file in argv:
        directory = os.getcwd()
        print(directory)
        os.remove(directory/file)
