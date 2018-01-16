
#! Python3
# Use regex to replicate the effects of strip().
# Remove white spaces automatically, and any other character specified in the argument.

import re


def strip_function(text):
	arg = ('[' + (input('Enter the character(s) to remove from the string:')) + ']')
	mo = re.sub(arg, '', text)
	mo = re.sub(r'[^\S]', '', mo)
	print(mo)


text = input('Enter your string to strip:')
# text = 'Through the fence, between the curling flower spaces, I could see them hitting.'
strip_function(text)
