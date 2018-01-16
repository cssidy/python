#! Python3


print('\n')
print('Wake up tamagotchi...')
print('\n')

# create game save, create save file?


tamagotchi1 = {
    'name': 'Peeko',
    'hungry': True,
    'weight': 10,
    'age': 1,
    'health': 'healthy',
    'mood': 'so-so',
    'photo': '(=^o.o^=)'
}


# egg hatch, add new tamagotchi to list
pets = [tamagotchi1]


def feed(pet):
    feeding = input('Feed the tamagotchi? yes or no:')
    # if hungry is True
    if pet['hungry']:
        # if feeding is yes
        if feeding == 'yes':
            pet['hungry'] = False
            pet['weight'] += 1
            print('Hunger satisfied.')
        # if feeding is no
        else:
            pet['weight'] -= 1
            print('This tamagotchi is starving!')
    # if hungry is False
    else:
        # if feeding is yes
        if feeding == 'yes':
            print('This tamagotchi is stuffed!')
            pet['weight'] += 1
        # if feeding is no
        else:
            print('Hunger level is okay.')

    # if tamagotchi weight is above 15, then it's overweight and has a 40% chance of getting sick and needing medicine
    # if tamagotchi weight is under 5, then it's underweight and has a 40% chance of getting sick and needing medicine


def mood(pet):
    # if hunger is False
    # if weight is 5 < x > 15
    # if health is healthy
        # then mood is happy

    # if hunger is True
    # or weight 5 < x > 15 is False
        # then mood is so-so

    # if health is sick
        # then mood is depressed
        # then tamagotchi can't play
    return True


def play(pet):
    # if mood is so-so or happy
        # initiate play
            # play graphic? chasing a ball?
            # mood = happy + 1
            # happy counter == 22
                # tamagotchi lays and egg
                # egg takes 22 days to hatch, then becomes another playable tamagotchi
                # choose to incubate the egg or discard it yes/no
            # tamagotchi weight - 1
    # if mood is depressed
        # then tamagotchi can't play
    return True


def health(pet):
    # if health is sick
        # then mood is depressed
        # then tamagotchi can't play
        # then tamagotchi won't eat

    # give medicine
        # if yes
            # tamagotchi mood is returned to so-so
            # health is returned to healthy
            # hunger is set to hungry

    # if health is healthy then do nothing
    return True


def age(pet):
    # inquire about system clock
    # mark day of tamagotchi birth, track age in number of days
    # if ays depressed is 55%+ tamagotchi has a 66% chance of dying any given day
    # if days depressed is 20% tamagotchi has a 5% chance of dying any given day
    # if days depressed is 10% tamagotchi has a 1% chance of dying any given day
    # if days depressed is 5% tamagotchi has a 0.1% chance of dying any given day
    return True


def egg(pet):
    # carrying an egg T/F
    # egg day counter, day + 1
    # egg day == 22
        # egg hatching
        # alert + graphic
        # create new tamagotchi stat list
        # add tamagotchi name to pet list
    # tamagotchi eggs...
    # if tamagotchi is just born, name it, assign it default stats

    # tamagotchi stats: name, age, weight, hunger, image
    # give tamagotchi food, medicine, play
    return True


for pet in pets:
    # display each tamagotchi stats list in a rjust(5) column
    print(pet['photo'])
    print(pet['name'])
    print('Age: ' + str(pet['age']))
    print('Weight: ' + str(pet['weight']))
    print('Condition: ' + str(pet['health']))
    print('Mood: ' + str(pet['mood']))
    print('\n')
    feed(pet)
    mood(pet)
    play(pet)
    health(pet)
    age(pet)
    # if there is an egg
    # egg(pet)
    # if changes are made to weight
    # print('Weight: ' + str(pet['weight']))
    # if midnight passes during game play, age + 1
