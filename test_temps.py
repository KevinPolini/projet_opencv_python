heure, minute = 0, 0


def decoupe(seconde):
    heure = seconde / 3600
    seconde %= 3600
    minute = seconde / 60
    seconde %= 60
    return (heure, minute, seconde)


print (decoupe(3600)) # la valeur entre parenthèse est à titre d'exemple