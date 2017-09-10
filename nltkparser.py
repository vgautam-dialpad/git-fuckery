
"""
Attempt at a python parser with NLTK
This is a chart parser with a pre-defined context-free grammar
Not as robust as the other one but MUCH less code!
"""

import nltk

grammar = nltk.CFG.fromstring("""
S -> VP | S 'and' S
VP -> VP_TRAN | VP_INTRAN
VP_INTRAN -> V_INTRAN
VP_TRAN -> VP_CREATURE | VP_INVENTORY | VP_OTHER
VP_CREATURE -> CARESS_V CREATURE_NP | ATTACK_V CREATURE_NP PP_IMPLEMENT | ATTACK_V CREATURE_NP
VP_OTHER -> V_OTHER NON_INVENTORIABLE
VP_INVENTORY -> INVENTORY_V INVENTORIABLE_NP | INVENTORY_V INVENTORIABLE_NP 'to inventory' | DROP_V INVENTORIABLE_NP | DROP_V INVENTORIABLE_NP 'from inventory'
PP_IMPLEMENT -> 'with' WEAPON_NP
INVENTORIABLE_NP -> WEAPON_NP | NON_WEAPON_NP
WEAPON_NP -> WEAPON | DET WEAPON
NON_WEAPON_NP -> NON_WEAPON | DET NON_WEAPON
WEAPON -> 'sword' | 'dagger' | 'flamethrower'
INVENTORY_V ->'take' | 'add' | 'inventory'
DROP_V -> 'drop' | 'leave'
NON_WEAPON -> 'mirror'
NON_INVENTORIABLE -> 'carpet'
CREATURE_NP -> CREATURE | DET CREATURE
CREATURE -> 'tiger' | 'rabbit' | 'horse' | 'elephant'
ATTACK_V -> 'kill' | 'destroy'
CARESS_V ->'caress' | 'pet' | 'pat'
V_INTRAN -> 'quit' | 'n' | 's' | 'e' | 'w' | 'u' | 'd'
DET -> 'the' | 'a' | 'an'
""")
parser = nltk.ChartParser(grammar)

def main():
    quit = False
    while not quit:
        sentence = input('Give me something to tokenize and parse ')
        tokenized = nltk.word_tokenize(sentence.lower())
        stopwordsfixed = [w for w in tokenized if w.isalpha()]
        trees = parser.parse_all(stopwordsfixed)
        if not trees:
            print("Cannot be parsed. Try again.")
        for tree in trees:
            print(tree)

if __name__ == "__main__":
    main()
