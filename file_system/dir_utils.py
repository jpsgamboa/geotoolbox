import os, glob

def create_dir_if_not_exists(fileDir):
    """
    Creates any missing folder in the provided directory.
    :param fileDir: the file directory
    :return: the created dir
    """

    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    return fileDir

def create_parent_dir_if_not_exists(fileDir):
    """
    Creates any missing folder in the provided directory up until the parent folder.
    Usefull for when the directory is a file.
    :param fileDir: the file directory
    :return: the parent dir
    """
    parentDir = os.path.dirname(fileDir)

    if not os.path.exists(parentDir):
        os.makedirs(parentDir)

    return parentDir


def delete_files_by_name(dir, name, name_is_wildcard):
    """
    Deletes any file matching inside the provided folder matching (or containing) the provided name.
    :param dir: the folder containing the files to be deleted
    :param name: the name to match
    :param name_is_wildcard: true if the name should be used as a wildcard
    """
    if name_is_wildcard:
        globParam = dir + "/" + "*" + name + "*"
    else:
        globParam = dir + "/" + name

    for filename in glob.glob(globParam):
        os.remove(filename)


def delete_dir(dir):
    """
    Recursively deletes the directory contents and removes the folder.
    :param dir:
    """
    clear_dir(dir,True)
    os.rmdir(dir)

def clear_dir(dir, recursive=False):
    """
    Clears the provided directory.
    :param dir:
    :param recursive: if true, subdirectories will be included
    """
    if not recursive:
        for filename in glob.glob(dir + "/*"):
            os.remove(filename)
    else:
        if (dir == '/' or dir == "\\"):
            return
        else:
            for root, dirs, files in os.walk(dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

def find_and_rename(dir, oldname, newName):
    """
    Utility to find a file in a given folder and rename it
    :param dir:
    :param oldname:
    :param newName:
    """
    for filename in os.listdir(dir):
        if filename == oldname:
            os.rename(filename, newName)