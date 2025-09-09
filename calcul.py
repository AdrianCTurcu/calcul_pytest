def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        raise ValueError("Impartirea la zero nu este permisa")
    return a / b

if __name__ == "__main__":
    print("Adunare 5 + 3 =", adunare(5, 3))
    print("Scadere 5 - 3 =", scadere(5, 3))
    print("Inmultire 5 * 3 =", inmultire(5, 3))
    print("Impartire 6 / 3 =", impartire(6, 3))
