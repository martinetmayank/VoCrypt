# To convert the generated ".WAV" audio file to ".MP3" format.

from writeMeta import addMeta


def convert(outputFile, input_file):
    """
    Converting .WAV file to .MP3.\n
    Arguments:\n
        outputfile: Output Filename.
        input_file: Name of input file.
    """
    from os import path
    from pydub import AudioSegment

    # Files
    sourceFile = input_file               # Setting the source file.
    destination = outputFile + ".mp3"   # Name of output file (MP3).

    # Convert "WAV" to "MP3"
    # Taking input to the audio file.
    sound = AudioSegment.from_wav(sourceFile)
    sound.export(destination, format="mp3")       # Exporting the file as MP3.

    # Adding metadata to the MP3 file.
    addMeta(destination)
    # cleanTemp(sourceFile)
