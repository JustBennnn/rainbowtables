"""Hashtable errors.

These are custom error messages.
"""
class HashtableException(Exception):
    """Base class for other custom exceptions."""
    pass

class FilenameError(HashtableException):
    """An invalid character, reserved name or an empty input in the filename."""
    pass

class PathError(HashtableException):
    """An invalid character or reserved name found in the path."""
    pass

class EncodingError(HashtableException):
    """The wordlist is unable to be decoded with the encoding entered."""
    pass

class AlgorithmError(HashtableException):
    """The algorithm they have tried to use is not supported."""
    pass

class SearchError(HashtableException):
    """Any errors given from the search function."""

class SystemNotSupported(HashtableException):
    """Unable to detect specific values for the current OS."""