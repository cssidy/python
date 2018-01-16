#! /usr/bin/python3
# passwordManager.py - An insecure password locker program.

import sys, pyperclip

PASSWORDS = {'Twitter': '325FJKJFNlknlknn#$#@#$%^&%$',
             'Facebook': '325FJKJFNlknlknn#$#@#$%^&%$',
             'Amazon': '325FJKJFNlknlknn#$#@#$%^&%$',
             'Mint': '325FJKJFNlknlknn#$#@#$%^&%$',
             'LinkedIn': '325FJKJFNlknlknn#$#@#$%^&%$',
             'Google': '325FJKJFNlknlknn#$#@#$%^&%$'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account)
