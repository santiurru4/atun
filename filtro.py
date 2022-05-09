import random

print(">>>FILTRANDO PALABRAS DE 5 LETRAS")

cant_5s=0
lista5=[]

with open("palabras5.txt", "w") as g:
    with open("listado.txt", "r", encoding="utf8") as f:
        for line in range (1290):
            f_datos = f.readline()
            if len(f_datos) == 6:
                cant_5s=cant_5s+1
                g.write(f_datos)
                lista5.append(f_datos.rstrip())
                #print(f_datos)

print(">>>OPERACION COMPLETADA CON EXITO")
print(">>>SE ENCONTRARON", cant_5s, "PALABRAS DE 5 LETRAS")
#print(lista5)
#----------------------------|ETAPA 2|------------------------------------------

solucion = random.choice(lista5)
print("La palabra aleatoria es", solucion)

palabra=str(input("Introduzca una palabra: "))
error_a=0
if len(palabra) == 5:
    print("es d 5")
    if palabra in lista5:
        print("en lista")
    else:
        error_a=error_a+1
        print("ERROR: La palabra introducida no esta en la lista. Por favor vuelva a ingresar una palabra.")
    #no hace falta verificar si tiene caracteres que no son letras porque no pertenecen a la lista
else:
    error_a=error_a+1
    print("ERROR:la palabra introducida no es de 5 letras. Por favor vuelva a ingresar una palabra.")
while error_a!=0:
    palabra=str(input("Introduzca una palabra: "))
    error_a=0
    if len(palabra) == 5:
        print("es d 5")
        if palabra in lista5:
            print("en lista")
        else:
            error_a=error_a+1
            print("ERROR: La palabra introducida no esta en la lista. Por favor vuelva a ingresar una palabra.")
        #no hace falta verificar si tiene caracteres que no son letras porque no pertenecen a la lista
    else:
        error_a=error_a+1
        print("ERROR:la palabra introducida no es de 5 letras. Por favor vuelva a ingresar una palabra.")