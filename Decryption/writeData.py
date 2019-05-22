# Write Output.

# A data set for refernece.
# Set of my Custom Keys.
myDict = {
    "A" : [637, 850, 524],
    "B" : [422, 1304, 729],
    "C" : [1001, 261, 677],
    "D" : [888, 293, 1211],
    "E" : [329, 786, 871],
    "F" : [349, 1075, 681],
    "G" : [391, 555, 3546],
    "H" : [440, 5992, 1448],
    "I" : [494, 999, 3001],
    "J" : [523, 759, 2551],
    "K" : [587, 429, 978],
    "L" : [659, 4333, 5592],
    "M" : [698, 1331, 343],
    "N" : [784, 1795, 2113],
    "O" : [880, 3839, 4002],
    "P" : [988, 2777, 2391],
    "Q" : [1028, 162, 3762],
    "R" : [1078, 888, 1477],
    "S" : [1105, 2355, 4097],
    "T" : [1139, 2549, 1717],
    "U" : [1187, 547, 1979],
    "V" : [1201, 299, 1807],
    "W" : [4233, 595, 2827],
    "X" : [1288, 228, 1023],
    "Y" : [1320, 187, 799],
    "Z" : [1379, 297, 513],
    " " : [5005, 5005, 5005],
    "," : [1665, 1665, 1665],
    "." : [3000, 3000, 3000]
}

def getKey(val):
    finalData = str()
    for key, value in myDict.items():
        if str(val) == str(value):
            print(key, end = " ")
            finalData += str(key)

    dataOutput(finalData)

def dataOutput(rawData):
    file = open("Decrypted Data.txt", "a")
    file.write(rawData)
    file.close()