# Encryption.

from notes import notes

#import optparse
"""
def parser():

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest = "filename", help = "Select the file to encode.")
    parser.add_option("-o", "--output", dest = "output", help = "Name of output file.")
    parser.add_option("-m", "--man", help = "")
    parser.add_option("-d", "--duration", help = "Set duration of beeps")

    (options, arguments) = parser.parse_args()"""

# Fuction to "open" and "process" the file.
def processFile(filename):
    global a        # Declaring global variable to store data.

    file = open(filename + ".txt", "r")     # Opening the file.
    a = file.read().upper()                 # Reading the file and converting all letters in CAPITALS and storing it in "string a". 
    print("Generating output for " + str(a))

    n = notes()
    n.hear(a)

# Main line to execute first.
if __name__ == "__main__":
    inputFile = input("Input file ---> ")
    a = ""
    processFile(inputFile)
