#! python3

print('How are you?')
feeling = input()
if feeling.lower() == 'great':
     print('I feel great too.')
else:
     print('I hope the rest of your day is good.')

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
    
    
  
def foo():
    """This is a multiline comment to help explain
    what the foo() function does."""
    print('Hello!')

spam = "Hello world!"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])


spam = 'Hello world!'
var1 = spam[0:5]
print(var1)

