
# Funktion utan beroenden
# allt den behöver finns antingen
# - i funktionen själv
# - i en parameter
def add(x, y):
    return x + y



# Funktion med beroenden
# den använder funktionen "add"
# Så länge som vi har ett separat test för "add", behöver vi inte testa den igen
def calculate(a, b, c, d):
    # vad blir (a+b) - (c+d) ?
    ab = add(a, b)
    cd = add(c, d)
    return ab - cd

