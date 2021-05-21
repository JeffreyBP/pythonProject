#sumatoria de cubos ingresando el n-esimo valor.
'''
1**3 =
1**3 + 2**3 =9
1**3 + 2**3 + 3**3= 36

'''
n = 0
sumatoria = 0

print('Ingrese el valor N de la cantidad de los primeros cubos a sumar: ')
n= int(input())

sumatoria = ((n*(n+1))/2)**2

print('La sumatoria cuando n es ', n, ' tiene con resultado: ', sumatoria)