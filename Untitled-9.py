#napis progtam kt nacita vstupny retazec a vytvori novy tak ze v nom zameni vsetky a za e

def zmena():
    vstup = input("napis vetu:")
    new=""
    for i in range(len(vstup)):
        if vstup[i]== "a":
            new += "e"
        else:
            new +=vstup[i]
    print(new)

zmena()