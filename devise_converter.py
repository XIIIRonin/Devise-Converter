def fromEuro():

    usd = 0.873591334
    livre = 1.27631694
    yuan = 0.134944527
    devise = str(input("USD (USD), Livres Sterling (L) ou Yuan (Y) ? : "))
    somme = str(float(input("Entrez votre somme en euro à convertir : ")))
    if devise == "USD":
        toUSD = float(somme) / float(usd)
        print(toUSD)
    elif devise == "L":
        toLivre = float(somme) / float(livre)
        print(toLivre)
    elif devise == "Y":
        toYuan = float(somme) / float(yuan)
        print(toYuan)


def fromUSD():
    euro = 1.1447
    livre = 1.46100
    yuan = 0.154471
    devise = str(input("Euro(E), Livres Sterling (L) ou Yuan (Y) ? : "))
    somme = str(float(input("Entrez votre somme en USD à convertir : ")))
    if devise == "E":
        toEuro = float(somme) / float(euro)
        print(toEuro)
    elif devise == "L":
        toLivre = float(somme) / float(livre)
        print(toLivre)
    elif devise == "Y":
        toYuan = float(somme) / float(yuan)
        print(toYuan)
        
        
def fromYuan():
    euro = 7.4158
    livre = 9.4632
    usd = 6.47375
    devise = str(input("Euro(E), Livres Sterling (L) ou USD (USD) ? : "))
    somme = str(float(input("Entrez votre somme en Yuan à convertir : ")))
    if devise == "USD":
        toUSD = float(somme) / float(usd)
        print(toUSD)
    elif devise == "L":
        toLivre = float(somme) / float(livre)
        print(toLivre)
    elif devise == "E":
        toEuro = float(somme) / float(euro)
        print(toEuro)


def fromLivre():
    euro = 0.78366
    yuan = 0.10567
    usd = 0.68456
    devise = str(input("Euro(E), Yuan (Y) ou USD (USD) ? : "))
    somme = str(float(input("Entrez votre somme en Livre Sterling à convertir : ")))
    if devise == "USD":
        toUSD = float(somme) / float(usd)
        print(toUSD)
    elif devise == "Y":
        toLivre = float(somme) / float(yuan)
        print(toLivre)
    elif devise == "E":
        toEuro = float(somme) / float(euro)
        print(toEuro)        


        
base = input("Voulez-vous convertir des Livres Sterling(L), des Yuans(Y), des Euros(E) ou des USD(USD) ? : ")

if base == "L":
    fromLivre()
elif base == "E":
    fromEuro()
elif base == "Y":
    fromYuan()
elif base == "USD":
    fromUSD()
