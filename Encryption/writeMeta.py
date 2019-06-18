# Add metadata.



def addMeta(input_file):
    """
    Adds metadata to the audio file.\n
    Arguments:\n
        filename: Name of the output file.
    """
    from mutagen.mp3 import MP3
    from mutagen.easyid3 import EasyID3
    import mutagen.id3

    # Opening the file KEY file to wite the metadate to MP3 file.
    file = open("key.txt", "r")
    key = file.read()   # Reading the file and storing it in "key" variable.

    # Opening the MP3 file
    mp3file = MP3(input_file, ID3=EasyID3)

    # Checking whether the tags exist or not by adding a tag.
    try:
        mp3file.add_tags(ID3=EasyID3)
    # If tag exists, then
    except mutagen.id3.error:
        print("has tags")

    mp3file['title'] = key  # Changing the "title" tag of the MP3 file.
    mp3file.save()      # Saving the MP3 file after changing its title.
    print(mp3file.pprint())
    # cleanTemp(file)