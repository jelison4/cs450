from random import shuffle
​
cards = [
    ["C in CIA", "confidentiality"],
    ["I in CIA", "integrity"],
    ["A in CIA", "availability"],
​
    ["First D in DAD", "disclosure"],
    ["A in DAD", "alteration"],
    ["Second D in DAD", "denial"],
​
    ["S in STRIDE", "spoofing"],
    ["T in STRIDE", "tampering"],
    ["R in STRIDE", "repudiation"],
    ["I in STRIDE", "impersonation"],
    ["D in STRIDE", "denial of service"],
    ["E in STRIDE", "elevation of privilege"],
​
    ["C in CARReLS", "commitment"],
    ["A in CARReLS", "authority"],
    ["R in CARReLS", "reciprocation"],
    ["Re in CARReLS", "reverse engineering"],
    ["L in CARReLS", "likening"],
    ["S in CARReLS", "scarcity"],
​
    ["T in TRIPP", "training"],
    ["R in TRIPP", "reaction"],
    ["I in TRIPP", "inoculation"],
    ["First P in TRIPP", "policy"],
    ["Second P in TRIPP", "physical"],
​
​
    ["First D in DREAD", "damage potential"],
    ["R in DREAD", "reproducability"],
    ["E in DREAD", "exploitability"],
    ["A in DREAD", "affected users"],
    ["Second D in DREAD", "discoverability"]
]
​
#osi layers

def run_test():
    shuffle(cards)
    tmp_cards = cards.copy()
    total = len(tmp_cards)
    correct = 0
​
    for i, card in enumerate(tmp_cards):
        print("{}: ".format(card[0]), end="")
        inp = input()
        if inp == card[1]:
            print("Good job!\n")
            cards.remove(card)
            correct += 1
        else:
            print("The answer was {}, try again.\n".format(card[1]))
​
    print("Your score: {}/{}".format(correct, total))
    
    if len(cards) > 0:
        print("Rerunning test...")
        run_test()
​
run_test()