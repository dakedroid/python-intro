# Mi primer Hola mundo
print("Hola Tec Mina")

# Variables
x = 4
nombreMessi = "MESSI"
nombreCristiano = "CRISTIANO"
z = float(3)
y = int(3.2)
k = int("10")
print(z)
print(y)
print(k)
print(type(z))
print(type(y))
print(type(k))

# Condiciones
if x == 7:
    print(nombreCristiano)
elif x == 10:
    print(nombreMessi)
elif x == 4:
    print("rafa marquez")
else:
    print("No Existe")

# Strings
nombre = "HOLA"
letra = nombre[0]
print(letra)

# CICLOS
for letra in nombre:
    print(letra)

# IMPRIMIR LONGITUD
print(len(nombre))

# COMPROBAR SI EXISTE UNA CADENA DENTRO DE STRING
texto = "alla en la fuente habia un chorrito"
print("chorrito" in texto)
if "chorrito" in texto:
    print("CHORRITO")

# DEL LA SIGUIENTE VARIABLE TEXTO =
"""
'SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR'
SI ENCUENTRA EL NUMERO 7 Y ES MENOR A 8
IMPRIMIR EL NUMERO 7 CONVERTIDO A INT 
Y EL TEXTO, ' ES HORA DE IRNOS SON LAS : '7'
"""

## Slicing String
b = "Hola Mundo"
# Slice por rango
print(b[5:10])
# Slice desde el inicio
print(b[:5])
# Slice desde una posicion hasta el final
print(b[5:])
# Slice con posiciones negativas
print(b[-5:-2])

# Boleanos
# Mayor que
print(10 > 9)
# igual que
print(10 == 9)
# menor que
print(10 < 9)
# variables boleanas
enStock = True
isTiendaAbierta = True
if enStock and isTiendaAbierta:
    print("VENDER PRODUCTOS")

tieneEfectivo = False
tieneTarjeta = True
if tieneTarjeta or tieneEfectivo:
    print("PAGO ACEPTADO")

regresasteConEx = False
if not regresasteConEx:
    print("MENTIROSO!")

paseLenguajes = True
if not paseLenguajes:
    print("REPROBASTE")

isUploaded = False
if isUploaded:
    print("")
else:
    print("REINTENTAR")

if not isUploaded:
    print("REINTENTAR")

# OPERADORES ARITMETICOS

x = 5
y = 6

# SUMA
print(x + y)

# RESTA
print(x - y)

# Multiplicacion
print(x * y)

# Division
print(x / y)

# Modulo
print(x % y)

# Exponentes
print(2 ** 2)
print(x ** 2)
print(x ** y)

# floor division
print(4 // 2)
print(x // y)

# Operadores de Asignación
x = 30
x += 32
x -= 2
x *= 2
x /= 2
print(x)

# Operadores Logicos
# de Comparacion
a = 3
b = 2

# Igual
print(a == b)
# Diferente
print(a != b)
# Mayor
print(a > b)
# Menor
print(a < b)
# Mayor igual
print(a >= b)
# Menor igual
print(a <= b)

# Operadores Logicos
promedio = 100
asistencias = True
aprobado = (promedio > 70) and asistencias
# and, or, not
print(aprobado)

# Operadores de identidad
j = "HOLA"
k = "HOLA "
print(j is k.replace(" ", ""))
print(j is not k)

# Operadores de pertenencia
print("A" in "HOLA")
print("A" not in "HOLA")

# Listas
frutas = ["Manzana", "Banana", "Mango"]
frutas2 = ["🍎", "🍌", "🥭"]
print(frutas)
print(frutas2)
lista = [1, 2, 3, 4, 5, 6]
logico = [True, False, True]
lista1 = ["abc", 34, True, 'a', "🍑"]
print(type(lista))
print(lista1)

# list, Tuple, Set, Dictionary
""" 
List: es una colección la cual esta ordenada
y modificable, la cual permite duplicados.

Tuple: Es una coleccion la cual esta ordenada y 
no es modificable. Permite duplicados

Set: Es una coleccion la cual NO❌ esta ordenada y
no es modificable ni indexada. No❌ permite Duplicados

Dictionary: Es una coleccion la cual esta ordenada
es modificable. No Permite duplicados.
"""
# Lista
lista1 = ["🐥", "🙊", "🐷", "🐷", "🐷"]
lista1.insert(3, "🐶")
lista1[2] = "🐯"
print(lista1)
# Tupla
tupla1 = ("🐥", "🙊", "🐷", "🐷")
print(tupla1)
# Set
set1 = {"🐥", "🙊", "🐷"}
set1.add("🐨")
set1.add("🐙")
print(set1)
# Diccionario
diccionario1 = {
    "pollo": "🐥",
    "monito": "🙊",
    "cerdito": "🐷"
}
diccionario1["koala"] = "🐨"
diccionario1["tigre"] = "🐯"
print(diccionario1["monito"])
print(diccionario1)

"""
#0 CREAR UNA LISTA : 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2. CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
   NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET 
   MAXIMO VALOR, MINIMO VALOR
#5. IMPRIMIR LAS ESTADISTICAS"""
numeros = [1, 2, 2, 3, 4, 4]
numerosSet = set(numeros)
sumaLista = sum(numeros)
sumaSet = sum(numerosSet)
len(numerosSet)
max(numeros)
min(numeros)

# CONDICIONES
a = 200
b = 33

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

# Ciclo while - mientras

quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron < 3:
    vecesRegresaron += 1
    print("Han Vuelto " + str(vecesRegresaron) + "Veces")

# Break
i = 8
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("error")



print("Continue")
# Continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Ciclo for  - for each
frutas = ["🍎", "🍌", "🥭"]
# for - Por cada
buscar = True
if buscar:
    for fruta in frutas:
        if fruta == "🍌":
            print("Se encontró: " + fruta)
        else:
            print("NO COINCIDE")
else:
    print("NO SE ESTA BUSCANDO")


