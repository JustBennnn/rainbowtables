"""Search the hash table.

This program is mainly for the search function.
"""
import base64
import json
import math
import os
import time
import zlib
from typing import Any, Tuple, Union

from .errors import SearchError
from .insert import hash_function1, hash_function2

__all__ = [
    "search"
]

def search(hash_string, hash_table_path, full_path=False, time_took=True, compression=False) -> Union[Tuple[str, str], str, bool]: #time_tooks is measured in seconds
    """Search through the hash table until we find a plaintext match to the hash given."""
    start_time = time.time()
    
    hash_table_path = hash_table_path + ".json"
    if full_path == False:
        hash_table_path = os.getcwd() + "/" + hash_table_path

    if os.path.isfile(hash_table_path) == False:
        raise FileNotFoundError("Create the directory (create_directory) and the file (create_file) before inserting.")

    hash_file = open(hash_table_path, "r")
    hash_file_content = hash_file.read()
    if compression == True:
        """Decompress the hash file content."""
        hash_file_content = hash_file_content.encode("utf-8")
        hash_file_content = base64.b64decode(hash_file_content)
        hash_file_content = zlib.decompress(hash_file_content)
        hash_file_content = hash_file_content.decode("utf-8")
    hash_file_content = json.loads(hash_file_content)
    hash_file.close()

    if hash_file_content == [{}, {}, {}, []]:
        raise SearchError("Insert data into the hash table before doing a lookup.")

    hash_dict1 = hash_file_content[0]
    hash_dict2 = hash_file_content[1]
    collision_dict = hash_file_content[2]
    hash_dict_length = len(hash_dict1)
    collision_dict_length = hash_file_content[3][0]

    hash_index1 = hash_function1(hash_string, hash_dict_length) 
    hash_index2 = hash_function2(hash_string, hash_dict_length)
    if collision_dict_length > 0:
        probe_limit = int(math.log(collision_dict_length, 2))
        hash_index3 = hash_function1(hash_string, collision_dict_length) #for the secondary table

    if hash_dict1 != {}:
        if hash_string == hash_dict1[hash_index1][0:hash_dict1[hash_index1].find(":")]:
            matching_plaintext = hash_dict1[hash_index1][(hash_dict1[hash_index1].find(":"))+1:len(hash_dict1[hash_index1])]
            end_time = time.time()

            if time_took == True:
                return (matching_plaintext, str(end_time-start_time))
            else:
                return matching_plaintext

    if hash_dict2 != {}:
        if hash_string == hash_dict2[hash_index2][0:hash_dict2[hash_index2].find(":")]:
            matching_plaintext = hash_dict2[hash_index2][(hash_dict2[hash_index2].find(":"))+1:len(hash_dict2[hash_index2])]
            end_time = time.time()

            if time_took == True:
                return (matching_plaintext, str(end_time-start_time))
            else:
                return matching_plaintext

    if collision_dict_length > 0:
        for x in map(str, range(int(hash_index3), int(hash_index3)+probe_limit+1)):
            if hash_string == collision_dict[x][0:collision_dict[x].find(":")]:
                matching_plaintext = collision_dict[x][collision_dict[x].find(":")+1:collision_dict[x].rfind(":")]
                end_time = time.time()

                if time_took == True:
                    return (matching_plaintext, str(end_time-start_time))
                else:
                    return matching_plaintext

    return False