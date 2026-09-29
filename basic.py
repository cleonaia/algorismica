# Problema 2.1

def convert_temp(temp_celsius) -> float: # no es None porque hace return asi que no puede ser None
    temp_celsius: float = float(input("Introdueix la temperatura de Celsius:"))

    temp_fahrenheit = (9 / 5) * temp_celsius + 32

    return temp_fahrenheit

temperatura_f = convert_temp()


# Problema de convertir

def convert0a50() -> List:
    list_temp_fahrenheit = []

    for temp_celsius in range(0, 51, 5):
        temp_fahrenheit = convert_temp(temp_celsius)
        list_temp_fahrenheit.append(temp_fahrenheit)

    return list_temp_fahrenheit

print(convert0a50()) 


# Problema 2.2

def futval(inversio, interes):
    principal = inversio
    for i in range(10):
        principal = principal * ( 1 + interes)
    return principal

futval(100, 0.1)


def futval2(inicial, anys, interesPerCent, comissioPerCent):
    #
    diners = inicial * (1 + interesPerCent) ** anys

    comissio = diners * comissioPerCent

    diners = diners - comissio

    return diners

print(futval2(1000, 5, 0.04, 0.03))


# Problema 2.3 Condicionals

def prouCerveses(nre_cerveses, es_cap_de_setmana):
    if es_cap_de_setmana:
        if nre_cerveses >= 50:
            return "Exit"
        else:
            return "Fracàs"
    else:
        if 50 <= nre_cerveses <= 100:
            return "Exit"
        else:
            return "Fracas"

assert prouCerveses(75, False) == "Èxit"


# Problema 2.3 Condicionals

def nota(nre):
    qualificacio : float = float(input("Introdueix la teva nota: "))

    if (nre <= 5):
        print("Ha suspès")
    elif (nre >= 5 or nre < 7):
        print("Has aprovat")
    elif (nre >= 7 or nre < 9):
        print("Has tret un notable")
    elif (nre >= 9 or nre < 10):
        print("Has tret un excel·lent")
    else:
        print("Has tret matricula d'honor")
    
    return qualificacio

assert nota(8.9) = 'Notable'

# Problema 2.4  Pendent d'una recta 

def pendent(x1, y1, x2, y2):

    m : float = (y2-y1)/(x2-x1)

    return m


def equacio(x1, y1, x2, y2):
    m = pendent(x1, y1, x2, y2)
    n = y1 - m * x1

    # terme x

    if m == 0:
        terme_x = ""
    elif m == 1:
        terme_x = "x"
    elif m == -1:
        terme_x = "-x"
    else:
        terme_x = str(m) + "x"

    # terme independent

    if n == 0:
        terme_n = ""
    elif terme_x == "":
        terme_n = str(n)
    elif n > 0:
        terme_n = " + " + str(n)
    else:
        terme_n = " - " + str(-n)

    # Cas m = 0 i n = 0

    if terme_x == "" and terme_n == "":
        equacio = "y = 0"
    else:
        equacio = "y = " + terme_x + terme_n

    print(equacio)


# Problema 2.5 Capicua

def es_capicua(paraula):

    cadena : str = str(input("Introdueix la paraula: "))
    


    return b_es-capicua





