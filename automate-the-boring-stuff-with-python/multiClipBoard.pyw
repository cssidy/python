#! Python3

# multiClipBoard.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe multiClipBoard.py save <keyword> - Saves clipboard to keyword.
#        py.exe multiClipBoard.py <keyword> - Loads keyword to clipboard.
#        py.exe multiClipBoard.py list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content

# TODO: List keywords and load content

mcbShelf.close()

