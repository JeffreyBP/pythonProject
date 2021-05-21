# ejercicio realizado por Yari
decimal = float(input("Ingrese por favor un número decimal: "))
entero1 = int(input("Ingrese por favor un número entero: "))
entero2 = int(input("Ingrese por favor un número entero: "))
entero3 = int(input("Ingrese por favor un número entero: "))

if decimal > entero1 and decimal > entero2 and decimal > entero3:
    print(f"El númeo mayor es: {decimal}")
if entero1 > decimal and entero1 > entero2 and entero1 > entero3:
    print(f"El número mayor es {entero1}")
if entero2 > decimal and entero2 > entero1 and entero2 > entero3:
    print(f"El número mayor es {entero2}")
if entero3 > decimal and entero3 > entero1 and entero3 > entero2:
    print(f"El número mayor es {entero3}")
print('Fin del programa')