"""Hashtable with worst case O(log n) lookup.

This hashtable works similarly to a rainbow table, where it stores plaintext values
with the corresponding hash, meaning you can 'reverse' the hash.

The main table uses the Cuckoo implementation, and any cycles from 
that table go to the secondary table, which uses the Robin Hood implementation.

Go to the README.md for usage.
"""
from .directories import *
from .errors import *
from .insert import *
from .search import *