# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar
# ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
num = int(input("Diga el número de palabras que va a introducir: "))
if num <= 0:
    print("¡Imposible!")
else:
    lista_palabras = []
    for x in range(num):
      palabras = str(input("Dime la palabra %s " % (x+1)))
      lista_palabras.append(palabras)
    print(lista_palabras)
    print(len(lista_palabras))

