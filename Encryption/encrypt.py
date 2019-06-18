# Encryption.

from notes import notes
from clean import del_file


# Fuction to "open" and "process" the file.
def processFile(filename):
    """
    Process all the initial data.\n
    Arguments:\n
        filename: Input file name.
    """
    global a        # Declaring global variable to store data.

    file = open(filename + ".txt", "r")     # Opening the file.
    # Reading the file and converting all letters in CAPITALS and storing it in "string a".
    a = file.read().upper()
    print("Generating output for " + str(a))

    n = notes()
    n.hear(a)


# Main line to execute first.
if __name__ == "__main__":
    inputFile = input("Input file ---> ")
    a = ""
    processFile(inputFile)
    del_file('key.txt')