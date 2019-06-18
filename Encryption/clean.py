# Cleans the temp data generated while encryption.


def del_file(filename):
    """
    Deletes a file.\n
    Arguments:\n
        filename: Name of the file to be deleted.
    """
    import os
    path = os.path.realpath(filename)

    if os.path.exists(path):
        os.remove(path)
    else:
        print("Path doesn't exist!!")
