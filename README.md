# rainbowtables

[![Downloads](https://pepy.tech/badge/rainbowtables)](https://pepy.tech/project/rainbowtables)
[![Downloads/Month](https://pepy.tech/badge/rainbowtables/month)](https://pepy.tech/project/rainbowtables)
[![PyPI Version](https://img.shields.io/pypi/v/rainbowtables)](https://pypi.org/project/rainbowtables/)
[![Last Commit](https://img.shields.io/github/last-commit/justbennnn/rainbowtables)](https://github.com/JustBennnn/rainbowtables/commits/master)
[![Repository Size](https://img.shields.io/github/repo-size/justbennnn/rainbowtables)](https://github.com/JustBennnn/rainbowtables)
[![License MIT](https://img.shields.io/github/license/justbennnn/rainbowtables)](https://github.com/JustBennnn/rainbowtables/blob/master/LICENSE)
[![Discord Profile](https://img.shields.io/badge/chat-discord-blue)](https://discordapp.com/users/801460768577945681)

Rainbowtables is a library where the user can create their own rainbowtable. This means that they can insert values
from a wordlist into the table and then do a lookup for a word based on its hash. It essentially finds a plaintext 
match for a hash inside of the table. The rainbowtable has a worst case lookup time of O(log n), where 'n' is the size
of the table, and a best case lookup time of O(1).

## installation
using [pip](https://pypi.org/project/rainbowtables "")

```
pip install rainbowtables
```

using setup.py to install

```
git clone https://github.com/justbennnn/rainbowtables.git
cd rainbowtables
python setup.py install
```

## usage
The following examples show the usage of every function in rainbowtables.

```python
import rainbowtables as rt

rt.set_directory("/rainbow_table", full_path=False)
rt.set_filename("demo_table")

rt.create_directory()
rt.create_file()

print("The set directory has been created at", rt.get_directory()) 
print("The set file has been created at", rt.get_filename(file_extension=True))
print("The full path of the file is", rt.get_full_path(file_extension=True))
```

> If `full_path` is set to false, then the directory given will be created in relation to the program directory. 
> If it is set to false, also remember the forward slash at the start of the directory name!

> When `file_extension` is set to true, then the program will return .json at the end of the filename.

```python
print(rt.supported_algorithms) #show the current supported algorithms
rt.insert("wordlist.txt", "sha256", wordlist_encoding="utf-8", display_progress=True, compression=True) #display_progress shows the current word being iterated
#or
wordlists = ["wordlist1.txt", "wordlist2.txt"]
rt.insert_wordlists(wordlists, "sha256", wordlist_encoding="utf-8", display_progress=True, compression=True) #this function inserts multiple wordlists at once
```

> When the insert function is called, it will use the current set file directory to insert into.
> Make sure to use `set_directory()` and `set_filename()` before insert is called, and in the same program.

> Both `wordlist_encoding` and `display_progress` are set to their default values in the example.
> However, the default value for `compression` is False.

The `insert` function will iterate through each word inside of the wordlist, and store its hash in the rainbowtable.\
The `insert_wordlists` function will do the same as the `insert` function, but also iterate through multiple wordlists to put into the rainbowtable.
The efficieny of this function is going to be improved in a future update.

```python
lookup = search(
    "97b7a2c97203792e932f1a2d26eb5b3f780ab9ec42e9f189186e6353d7564a2c", 
    "demo_table", #this could also rt.get_full_path(), with full_path set to True
    full_path=False, #full_path default value is False
    time_took=True, #time_took default value is True
    compression=True) #compression should only be True if the insert function compressed the table

if lookup != False:
    print("The decrypted hash is", lookup[0] + ".") #output - The decrypted hash is https://www.youtube.com/watch?v=iik25wqIuFo.
    print("It was found in", lookup[1], "seconds.") #output - It was found in 0.5 seconds.
```

> If `full_path` is set to false, and the rainbowtable is in the current directory, set the path as shown above in the example.

> Otherwise, if it is in a directory and `full_path` is set to false, enter the directory as normal, but remember the forward slash
> at the start.

The `search` function will return 1 of 3 results. 
* The matching plaintext.
* A tuple containing the matching plaintext and the time taken to find it.
* False, meaning the lookup failed.