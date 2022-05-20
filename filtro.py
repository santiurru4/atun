import random
#----------------------------|ETAPA 1|------------------------------------------
print(">>>FILTRANDO PALABRAS DE 5 LETRAS")

cant_5s=0                                   #numero de palabras de 5 letras
lista5=[]                                   #Lista de palabras

with open("palabras5.txt", "w") as g:       #para guardar las palabras en un archivo .txt aparte
    with open("listado.txt", "r", encoding="utf8") as f:
        for line in range (1290):
            f_datos = f.readline()
            if len(f_datos) == 6:
                cant_5s=cant_5s+1
                g.write(f_datos)            #para guardar las palabras en un archivo .txt aparte
                lista5.append(f_datos.rstrip())
                #print(f_datos)

print(">>>OPERACION COMPLETADA CON EXITO")
print(">>>SE ENCONTRARON", cant_5s, "PALABRAS DE 5 LETRAS")
#print(lista5)
#----------------------------|ETAPA 2|------------------------------------------

solucion = random.choice(lista5)
print("La palabra aleatoria es", solucion)
palabra=input("Introduzca una palabra: ")
def pregunta(q):
    while q not in lista5:
        print("ERROR:La palabra no está en el diccionario")
        if len(q) != 5:
            print("ERROR:la palabra introducida no es de 5 letras. Por favor vuelva a ingresar una palabra.")
        if not q.isalpha():
            print("ERROR:Contiene caracteres especiales")
        q=input("Introduzca una palabra: ")
        print(q)

#----------------------------|ETAPA 3|------------------------------------------
devolucion=[]
#a=solucion
#B=intento
def comparador(a,b):
    for i in range(5):
        x=a[i]
        y=b[i]
        if x==y:
            devolucion.append(y)#Verde
        elif y in a:
            devolucion.append(y)#Amarillo
        else:
            devolucion.append(y)#Rojo/gris
#solucion=str(input("solucion:"))
#intento=str(input("intento:"))
def respuesta(m):
    qqq="".join(m)
    print(qqq)

respuesta(devolucion)
while solucion!=palabra:
    pregunta(palabra)
    comparador(solucion,palabra)
    respuesta(devolucion)