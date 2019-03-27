#Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

num = int(input("Diga el número de palabras que va a introducir: "))
if num <= 0:
    print("¡Imposible!")
else:
    lista_palabras = []
    for x in range(num):
      palabras = str(input("Dime la palabra %s " % (x+1)))
      lista_palabras.append(palabras)
    print(lista_palabras)
    palabra = str(input("Digame la palabra que quiere contar: "))
    count = 0
    for i in lista_palabras:
        if i == palabra:
            count = count +1
    if count == 0:
         print("La palabra no está en la lista")
    else:
         print("La palabra aparece %s" % (count + 1) + " veces")



