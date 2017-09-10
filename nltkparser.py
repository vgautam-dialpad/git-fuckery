
# Attempt at a python parser with NLTK

import nltk

grammar = nltk.CFG.fromstring("""
S -> VP
VP -> V_TRAN OBJ | V_INTRAN
OBJ -> 'tiger' | 'rabbit' | 'horse' | 'elephant'
V_TRAN -> 'kill' | 'destroy' | 'caress' | 'pet' | 'pat'
V_INTRAN -> 'quit' | 'n' | 's' | 'e' | 'w'
""")
parser = nltk.ChartParser(grammar)

"""
S → NP VP
NP → Det N | Det N PP
VP → V | V NP | V NP PP
PP → P NP

Det → 'the' | 'a'
N → 'man' | 'park' | 'dog' | 'telescope'
V → 'saw' | 'walked'
P → 'in' | 'with'

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
"""

def main():
    quit = False
    while not quit:
        sentence = input('Give me something to tokenize and parse ')
        tokenized = nltk.word_tokenize(sentence.lower())
        stopwordsfixed = [w for w in tokenized if w.isalpha()]
        trees = parser.parse_all(stopwordsfixed)
        for tree in trees:
            print(tree)

if __name__ == "__main__":
    main()
