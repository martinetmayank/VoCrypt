# To convert the generated ".WAV" audio file to ".MP3" format.

from writeMeta import addMeta
from clean import cleanTemp

def convert(outputFile, filename):
    from os import path
    from pydub import AudioSegment

    # Files
    sourceFile = filename               # Setting the source file.
    destination = outputFile + ".mp3"   # Name of output file (MP3).

    # Convert "WAV" to "MP3"
    sound = AudioSegment.from_wav(sourceFile)       # Taking input to the audio file.
    sound.export(destination, format = "mp3")       # Exporting the file as MP3.

    addMeta(destination)
    #cleanTemp(sourceFile)
