from tinytag import TinyTag
from writeData import getKey

# Processing the audio file and its metadata.
def processData(file):
    global temp         # temp variable to store the data.
    global keyList      # Final keyList  -- Organized -- Set of 3.
    global tempKeys     # Temp keylsit -- Unorganized -- Set of 1.

    # Initializing the "lists" and "strings" to store data.
    tempKeys = list()       # Temp keylsit -- Unorganized -- Will be Set of 1.
    temp = str()            # temp variable to store the data.
    keyList = list()        # Final keyList  -- Organized -- Set of 3.

    data = TinyTag.get(file)        # Reading the file.
    keys = data.title       # Storing the metadata in variable KEYS.

    # Appending all the metadata in a temporary list -- tempKEYS.
    for i in keys:
        tempKeys.append(i)

    for j in tempKeys:
        if j != " ":
            temp += str(j)
        elif j == " ":
            keyList.append(temp)
            temp = ""
    #print(keyList)
    newData(keyList)

# To organize data in an easy readable format as 3 set of frequencies.
def newData(keyList):
    global newList
    newList = list()        # A new list to store set of "3 Frequencies".
    newTemp = str()
    i = 0   # Initializing the counter value.
    j = 1   # Initializing the counter value.
    for elements in keyList:

        if i % 3 == 0:
            newTemp += str("[")

        newTemp += str(elements)
        i = i + 1   # Initial value is 1.

        if i != (3 * j):
            newTemp += str(",")
            newTemp += str(" ")

        # Divivding the parts of list in set of 3 to get desired output.
        if i == int(3 * j):
            newTemp += str("]")
            newList.append(newTemp)     # Appending all the "3 subsets" to make 1 "Super Set".
            newTemp = ""
            j = j + 1

    print("Your data has been decrypted")
    for i in newList:
        #print(i)
        values = i
        getKey(values)