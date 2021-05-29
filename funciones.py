# codigo Hernan

categoria = ""
 # creacion de funcion
def categorizacion():
  edad = int(input("sr usario por favor ingrese la edad:" ))
  if 1 <= edad <= 4:
    categoria = "bebe"
  elif 5 <= edad <= 12:
    categoria = "niño"
  elif 13 <= edad <= 18:
    categoria = "adolescente"
  elif 19 <= edad <= 28:
    categoria = "joven"
  elif 29 <= edad <= 40:
    categoria = "adulto joven"
  elif 41 <= edad <= 67:
    categoria = "adulto"
  else:
    categoria = "adulto mayor"
  # salida esperada
  return print("su categori es: ",categoria)


#Llamado de función
categorizacion()


# inicialización de variables
n = 0
lista =[]
i = 0
valor = 0
n = int(input(" Favor ingrese la longitud de la lista: "))
print("El tamaño de la lista es: ", n)
for jamon in range(n):
  valor = input("Apreciado usuario favor ingrese el valor de la lista en la pocisión: ")
  lista.append(valor)

# Resultados
print("Su lista de tamaño ",n," :",lista)
categorizacion()


#lista1=[1,2,3,4]
items= [2,4,6,8,10,12]
suma_pos = 0
for itera in items:
  suma_pos += itera
  print(" $",suma_pos, end="  " )

categorizacion()



