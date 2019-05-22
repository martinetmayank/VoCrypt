import toAudio
from converter import convert

# Set of my Custom Keys.
A = [637, 850, 524]
B = [422, 1304, 729]
C = [1001, 261, 677]
D = [888, 293, 1211]
E = [329, 786, 871]
F = [349, 1075, 681]
G = [391, 555, 3546]
H = [440, 5992, 1448]
I = [494, 999, 3001]
J = [523, 759, 2551]
K = [587, 429, 978]
L = [659, 4333, 5592]
M = [698, 1331, 343]
N = [784, 1795, 2113]
O = [880, 3839, 4002]
P = [988, 2777, 2391]
Q = [1028, 162, 3762]
R = [1078, 888, 1477]
S = [1105, 2355, 4097]
T = [1139, 2549, 1717]
U = [1187, 547, 1979]
V = [1201, 299, 1807]
W = [4233, 595, 2827]
X = [1288, 228, 1023]
Y = [1320, 187, 799]
Z = [1379, 297, 513]

space = [5005, 5005, 5005]
comma = [1665, 1665, 1665]
fullStop = [3000, 3000, 3000]

class notes:

    def hear(self, sentence = None):
        #print(sentence)
        global write_text
        # Making a variable to store all the data of frequencies.
        write_text = ""

        for text in sentence:
            out = [50, 50, 50]      # Setting the defult/temp value of "out".

            # Set of English Alphabets.
            if text == "A":
                out = A
            elif text == "B":
                out = B
            elif text == 'C':
                out = C
            elif text == 'D':
                out = D
            elif text == 'E':
                out = E
            elif text == 'F':
                out = F
            elif text == 'G':
                out = G
            elif text == 'H':
                out = H
            elif text == 'I':
                out = I
            elif text == 'J':
                out = J
            elif text == 'K':
                out = K
            elif text == 'L':
                out = L
            elif text == 'M':
                out = M
            elif text == 'N':
                out = N
            elif text == 'O':
                out = O
            elif text == 'P':
                out = P
            elif text == 'Q':
                out = Q
            elif text == 'R':
                out = R
            elif text == 'S':
                out = S
            elif text == 'T':
                out = T
            elif text == 'U':
                out = U
            elif text == 'V':
                out = V
            elif text == 'W':
                out = W
            elif text == 'X':
                out = X
            elif text == 'Y':
                out = Y
            elif text == 'Z':
                out = Z

            # Space, Comma and FullStop(s)
            elif text == " ":
                out = space
            elif text == ",":
                out == comma
            elif text == ".":
                out = fullStop
            #print(out)

            for i in out:
                toAudio.sineWave(i)
                toAudio.silence()
                write_text += str(i) + " "

        #print(write_text)

        # Enter the name of OUTPUT file
        outputFile = input("Enter the name of output file ---> ")
        filename = outputFile + ".wav"  # Adding extensions to output file.
        toAudio.saveAudio(filename)     # Saving the audio to the OUTPUT file.
        self.writeText(write_text)      # Writing all the frequnecies set.
        convert(outputFile, filename)   # Convertingt the WAV file to MP3 file.

    # A function to create a text file with all the frequesncies set.
    def writeText(self, write_text):
        file = open("key.txt", "w")     # opening and creating the file.
        file.write(write_text)          # Writing in the file created.
