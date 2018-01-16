#! python3
# strongPasswordDetection.py uses regex to determine if a given input has at least eight characters, contains both uppercase and lowercase
# characters and contains at least one digit.



import re


passwordRegex = re.compile(r'''(       # match must meet all of these requirements:
    ^
    (?=.*[A-Z])                        # at least one capital letter
    (?=.*[a-z])                        # at least one lower case letter
    (?=.*[0-9])                        # at least one numeral
    (?=.*[!@#$%^&*])                   # at least one special character
    .{8,}                              # at least eight characters
    $
    )''', re.VERBOSE)


def strength_test():
    password = input('Enter your password:')
    if passwordRegex.search(password):
        print('Password is secure.')
    else:
        print('Password is insecure.')

strength_test()
