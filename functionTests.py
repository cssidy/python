def hi(name):
    if name == 'Cassidy':
        print('Hello, Cassidy.')
    else:
        print('Hello, stranger!')
        response = input('Would you like to register in our system? (Y/N)')
        if response == 'Y':
            print('Great!')
        elif response == 'N':
            print('I never liked you anyways!!!')
        else:
            print('I fail to understand.')


hi(input('What is your name?'))
