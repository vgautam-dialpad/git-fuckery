
# Attempt at a python parser

import re

regex = r'[!,\.\s]+'
delimiters = re.compile(regex)

motion = set(['n', 'w', 'e', 's', 'd', 'u'])

inventory = set(['take', 'add', 'inventory'])
drop = set(['leave', 'drop'])
kill = set(['destroy', 'kill'])
caress = set(['caress', 'pet', 'pat'])
actions = inventory.union(drop).union(kill).union(caress)

creatures = set(['tiger', 'rabbit', 'horse', 'elephant', 'baboon']) # add more
things = set(['sword', 'dagger', 'flamethrower', 'mirror', 'carpet'])
objects = creatures.union(things)

negativeset = set(['never', 'not', 'don\'t'])


def move(string):
    print("Moving ", string);
    # Print new location's message
    # Update creatures encountered, other locations, etc

def parse(negation, verb, thing):
    if negation:
        print("not " + str(verb) + "ing " + str(thing))
    else:
        print(verb, thing)

def main():
    quit = False
    while not quit:
        sentence = input('Give me something to tokenize and parse ')
        negation = False
        curr_action = 0
        curr_object = 0
        lowercase = sentence.lower()
        sentence_split = re.split(delimiters, lowercase)
        for i in range(len(sentence_split)):
            token = sentence_split[i]
            if token == 'quit':
                quit = True
            elif token in negativeset:
                negation = True
            elif token in motion:
                move(token)
            elif token in actions:
                curr_action = token
            elif token in objects:
                curr_object = token
                if (curr_action and curr_object):
                    parse(negation, curr_action, curr_object)

if __name__ == "__main__":
    main()
