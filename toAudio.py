
# To make an audio output.

import math
import wave
import struct

from converter import convert    # My library to convert WAV to MP3.

# Audio will be contained in the list. Each frequcy will be appended here.
final_audio = list()
sampleRate = 48000.0    # Other standard values are 44.1K, 88.2K, 96K.

# The wave generated is a "sine" wave.
def sineWave(frequency = None, duration = None, amplitude = None):
    # Using global variables to store in the list created above.
    global final_audio

    # Set the default frequency.
    if frequency == None:
        frequency = 560

    # Set the default duration of wave.
    if duration == None:
        duration = 100

    # Set the default amplitute of wave.
    if amplitude == None:
        amplitude = 0.6

    numberSamples = int(duration * (sampleRate / 1000.0))   # Deciding the time span of per part of wave.

    # A mathematical equation to create SINEWAVE.
    for x in range(0, numberSamples):
        final_audio.append(amplitude * math.sin(2 * math.pi * frequency * (x / sampleRate)))

    return

# To add a pause if needed.
def silence(duration = None):

    """
    To add silence, just set the frequncy and amplitude to "0".
    """
    # Setting the amplitude to 0.
    amplitude = 0
    frequency = 0

    if duration == None:
        duration = 250

    numberSamples = int(duration * (sampleRate / 1000.0))

    for x in range(0, numberSamples):
        final_audio.append(amplitude * math.sin(2 * math.pi * frequency * (x / sampleRate)))

    return

# A function to save the audio generated in a file.
def saveAudio(filename = None):

    # Creating a new wavefile (for output) with some file name.
    if filename == None:
        filename = "output.wav"

    # Opening the file in "write" mode.
    file_wave = wave.open(filename, "w")

    # Setting the parmaeters for the wave file.
    nframes = len(final_audio)
    sampwidth = 2
    nchannels = 1
    comptype = "NONE"               # Compression Type
    compname = "not compressed"     # Compression Name

    file_wave.setparams((nchannels, sampwidth, sampleRate, nframes, comptype, compname))

    for pitch in final_audio:
        file_wave.writeframes(struct.pack("h", int(pitch * 32767)))

    file_wave.close()

    return