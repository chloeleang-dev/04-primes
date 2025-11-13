"""
module premier
"""
from math import sqrt



#### Fonction secondaire


def isprime(p):
    """
    
    Vérifier si un entier est un nombre premier ou pas.
    
    Args:
        t: nombre entier 
        p: nombre entier

    Returns:
        True ou False
    """

    if p <= 1:
        return False
    t = int(sqrt(p)) + 1
    premier = True

    while t>2:
        t = t-1
        if p%t == 0:
            premier = False

    # if premier == True:
    #     return True
    # else:
    #     return False

    return premier

#### Fonction principale


def main():

    """
    main 
    """

    # vos appels à la fonction secondaire ici
    print(isprime(8))
    print(isprime(7))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
