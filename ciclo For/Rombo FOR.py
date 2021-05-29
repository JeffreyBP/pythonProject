def rombo(n):
    for i in range(n):
        suma= "-".join(chr(ord('a')+n -j -1) for j in range(i+1))
        print((suma+suma[::-1][1:]).center(n*4-3,'-'))
    for i in range(n-1):
        suma = "-".join(chr(ord('a') + n - j - 1) for j in range(n-i - 1))
        print((suma + suma[::-1][1:]).center(n * 4 - 3, '-'))

n = int(input("Ingrese el valor entero para dibujar el rombo: "))
rombo(n)
print("miguel")