"""Manage the directories

This includes options to store the hashtable in a file or keep 
it temporarily, where it will be returned from the function...
"""
import json
import os
import platform
from typing import Tuple, Union

from .errors import FilenameError, PathError, SystemNotSupported

__all__ = [
    "set_directory",
    "set_filename",
    "get_directory",
    "get_filename",
    "get_full_path",
    "create_directory",
    "create_file"
]

directory = os.getcwd()
filename = "hash_table.json"

def check_for_invalid_characters(string, os, path_input=False) -> Tuple[bool, str]:
    """Give an error if any illegal characters are detected based on the os.
    
    Forward and back slashes will be ignored since they are used to define each section in a path.
    """
    if os == "Windows":
        if path_input == True:
            illegal_characters = ["<", ">", ":", '"', "|", "?", "*"]
        elif path_input == False:
            illegal_characters = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]

    elif os == "Linux":
        if path_input == False:
            illegal_characters = ["/"]
        else:
            return (False, "")

    for character in illegal_characters:
        if character in string:
            if character == ":":
                for x in range(0, len(string)):
                    if string[x] == ":" and x != 1:
                        return (True, ":")
            else:
                return (True, character)
    return (False, "")

def check_for_reserved_names(string, os) -> Tuple[bool, str]:
    """Give an error if any reserved names are used in the file path."""
    if os == "Windows":
        illegal_names = [
            "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", 
            "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1",
            "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        ]
    elif os == "Linux":
        """Linux has no reserved names."""
        return (False, "")
    else:
        raise SystemNotSupported(f"Unsupported OS {os}.")

    """An exception should only be given if an illegal name is found on its own with no other characters."""
    for reserved_name in illegal_names:
        if string.upper() == reserved_name:
            return (True, reserved_name)

        if reserved_name in string.upper():
            reserved_name_index = string.upper().find(reserved_name)

            if string[reserved_name_index-1] == "\\" or string[reserved_name_index-1] == "/":
                if reserved_name_index+(len(reserved_name)-1) == len(string)-1:
                    return (True, reserved_name)

                if string[reserved_name_index+len(reserved_name)] == "\\" or string[reserved_name_index+len(reserved_name)] == "/":
                    return (True, reserved_name)

    return (False, "")

def set_directory(file_directory, full_path=False) -> None:
    """Sets the directory of where the file will be stored. If 'full_path' is true,
    set the directory as the full path.

    If no directory is set, the file will be stored in the program location.
    """
    global directory

    invalid_characters = check_for_invalid_characters(file_directory, platform.system(), path_input=True)
    if invalid_characters[0] == True:
        raise PathError(f"Invalid character ({invalid_characters[1]}) found in file path.")

    reserved_names = check_for_reserved_names(file_directory, platform.system())
    if reserved_names[0] == True:
        raise PathError(f"OS reserved name ({reserved_names[1]}) found in file path.")

    if full_path == False:
        directory = directory + file_directory

    elif full_path == True:
        directory = file_directory

def set_filename(file_name) -> None:
    """Sets the filename.
    
    If no filename is set, it will remain the default name..
    """
    global filename

    file_name = file_name.strip()
    if file_name == "":
        raise FilenameError("The filename cannot be set as an empty value.")

    invalid_characters = check_for_invalid_characters(file_name, platform.system())
    if invalid_characters[0] == True:
        raise FilenameError(f"Invalid character ({invalid_characters[1]}) found in filename.")

    reserved_names = check_for_reserved_names(file_name, platform.system())
    if reserved_names[0] == True:
        raise FilenameError(f"OS reserved name ({reserved_names[1]}) found in filename.")
    
    filename = file_name + ".json"

def get_directory() -> str:
    """Returns the current set directory."""
    return directory

def get_filename(file_extension=False) -> str:
    """Returns the current set filename."""
    if file_extension == False:
        return filename[0:filename.find(".json")]
    else:
        return filename

def get_full_path(file_extension=True) -> str:
    """Returns the current set directory and filename."""
    return get_directory() + "/" + get_filename(file_extension=file_extension)

def create_directory() -> None:
    """Creates the set/default directory."""
    slash_indexes = []
    for x in range(0, len(directory)):
        if directory[x] == "/" or directory[x] == "\\":
            slash_indexes.append(x)
    
    directories_to_create = []
    for x in range(0, len(slash_indexes)):
        if x == len(slash_indexes)-1:
            if os.path.isdir(directory[0:len(directory)]):
                existing_directory = directory[0:len(directory)]
            else:
                directories_to_create.append(directory[0:len(directory)])

        else:     
            if os.path.isdir(directory[0:slash_indexes[x+1]]):
                existing_directory = directory[0:slash_indexes[x+1]]
            else:
                directories_to_create.append(directory[0:slash_indexes[x+1]])

    for _dir in directories_to_create:
        os.mkdir(_dir)

def create_file(overwrite_existing=False) -> Union[bool, None]:
    """Creates the file inside of the set/default directory.
    
    Only proceed if the set/default directory exists.
    """
    if os.path.isfile(get_full_path()):
        if overwrite_existing == False:
            return False

    if os.path.isdir(directory):
        file_path = get_full_path()
        create_file = open(file_path, "w")
        create_file.write(json.dumps([{}, {}, {}, []]))
        create_file.close()
    
    else:
        raise PathError("The directory must be created (.create_directory()) before the file is.")