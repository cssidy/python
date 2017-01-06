#! python3

string = ("The moose ran in front of my car, and almost took out an eagle swooping down to catch a rat, "
          "but I swerved and narrowly missed a snake, but then a coyote jumped on my windshield with a squirrel in "
          "its mouth and I crashed. Ah, Vermont.")
keywords1 = 'moose'
keywords2 = 'snake'
keywords3 = 'eagle'
keywords4 = 'coyote'

# determines if multiple keywords are found within a string

def keyword_match(string):
    s = "\n".join(string)
    for k in keywords1 or k2 in keywords2 or k3 in keywords3 or k4 in keywords4:
        if k or k2 or k3 or k4 in s:
            result = True
            print(result)
            print('Keyword match %')
            print('\n')
            break
        else:
            result = False
            print(result)
            print('No keyword match %')
            print('\n')
            break


keyword_match(string)
Contact GitHub API Training Shop Blog About
