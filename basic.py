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
    b_es_capicua = paraula == paraula[::-1]
    return b_es_capicua

def es_capicua(paraula):
    b_es_capicua = True
    n = len(paraula)
    for i in range(n // 2):
        if paraula[i] != paraula[n - 1 - i]:
            b_es_capicua = False
    return b_es_capicua

# Problema 2.6 Palindrom

import itertools

def generar_palindrom(cadena):
    palindroms = set()
    for p in itertools.permutations(cadena):
        paraula = "".join(p)
        if paraula == paraula[::-1]:
            palindroms.add(paraula)
    return sorted(palindroms)

# Problema 2.7 Divisors 

def divisors(num):
    petits = []
    grans = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            petits.append(i)
            if i != num // i:
                grans.append(num // i)
        i += 1
    return petits + grans[::-1]

#  Problema 2.8 Factorial menor

def factorial_menor(num):
    factorials = []
    factorial = 1
    i = 1

    while factorial < num:
        factorial * = 1

        if factorial < num:
            factorials.append(factorial)

        i += 1

    return factorials

assert factorial_menor(20) == [1, 2, 6]


# Problema 2.9 Minim i maxim 

def minim_maxim(llista):
    minim = llista[0]
    maxim = llista[0]

    for i in range(1, len(llista)):
        if llista[i]<minim:
            minim = llista[i]

        if llista[i] > maxim:
            maxim = llista[i]

    return minim, maxim

assert minim_maxim([3, 1, 5, 2, 7, 8]) == (1, 8)
assert minim_maxim([1, 7, 4, 6, 8, -2, 9, 5]) == (-2, 9)

print(minim_maxim([1, 7, 4, 6, 8, -2, 9, 5]))


# Problema 2.10 Sumatori de parelles

def sumatori_parelles(llista, valorSuma):
    parelles = []
    ordenada = sorted(llista)
    esq = 0
    dre = len(ordenada) - 1
    while esq < dre:
        suma = ordenada[esq] + ordenada[dre]
        if suma == valorSuma:
            parelles.append((ordenada[esq], ordenada[dre]))
            esq += 1
            dre += 1
        elif suma < valorSuma:
            esq += 1
        else:
            dre -= 1
    return parelles

assert sumatori_parelles([3,1,5,2,7,8], 10) == [(2, 8), (3, 7)]


# Problema 2.11 Sumes i quadrats

def suma_quadrats( n = 100 ):
    quadrats = [i**2 for i in range( 1, n+1)]
    suma_dels_quadrats = sum(quadrats)

    naturals = [i for i in range(1, n + 1)]
    quadrats_de_la_suma = sum(natural) ** 2

    diferencia = quadrats_de_la_suma - suma_dels_quadrats
    return diferencia

assert suma_quadrats() == 251644150

# Problema 2.12 Nombres amics

def suma_divisors(n):
    if n <= 1:
        return 0
    suma = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            suma += d
            if d != n // d:
                suma += n // d
        d += 1
    return suma

def amics(nre1, nre2):
    sonAmics = suma_divisors(nre1) == nre2 and suma_divisors(nre2) == nre1
    return sonAmics

assert amics(220, 284) == True
assert amics(200, 230) == True

# Problema 2.13 Nombres perfectes

def suma_divisors(n):
    if n <= 1:
        return 0
    suma = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            suma += d
            if d != n // d:
                suma += n // d
        d += 1
    return suma

def perfecte(nre):
    es_perfecte = nre > 1 and suma_divisors(nre) == nre
    return es_perfecte

assert perfecte(6) == True
assert perfecte(8) == False

# Problema 2.14 Avet

def avet(nre):
    files = (nre + 1) // 2
    for i in range(1, files + 1):
        espais = files - i 
        asterisc = 2 * i - 1
        for _ in range(espais):
            print('', end='')
        for _ in range(asterisc):
            print("*", end='')
        print()

avet(7)


