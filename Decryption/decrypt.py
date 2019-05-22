# Read Metadata.
from processData import processData
from writeData import getKey

if __name__ == "__main__":

    # Input the audio file not with extension
    file = input("Enter the audio file ---->" )
    file = file + ".mp3"    # Adding extenstion to audio file.
    print("The file to be processed is --->  " + str(file))     # Printing the file name.
    processData(file)      # Processing the audio file.