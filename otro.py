print(">>>FILTRANDO PALABRAS DE 5 LETRAS")

cant_5s=0
lista5=[]


with open("palabras5.txt", "w") as g:
    with open("listado.txt", "r", encoding="utf8") as f:
        largo=len(f.readlines())
        print("largo:",largo)
        for line in range (largo):
            f_datos = f.readline()
            if len(f_datos) == 6:
                cant_5s=cant_5s+1
                g.write(f_datos)
                lista5.append(f_datos.rstrip())
                #print(f_datos)

print(">>>OPERACION COMPLETADA CON EXITO")
print(">>>SE ENCONTRARON", cant_5s, "PALABRAS DE 5 LETRAS")
print(lista5)