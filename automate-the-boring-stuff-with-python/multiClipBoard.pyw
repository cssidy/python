#! Python3

# multiClipBoard.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe multiClipBoard.py save <keyword> - Saves clipboard to keyword.
#        py.exe multiClipBoard.py <keyword> - Loads keyword to clipboard.
#        py.exe multiClipBoard.py list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('multiClipBoard')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: List keywords and load content

mcbShelf.close()

