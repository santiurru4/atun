if __name__=="__main__":
    import random
    import colorama 
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    #----------------------------------------|ETAPA 1|------------------------------------------
    #print(">>>FILTRANDO PALABRAS DE 5 LETRAS")

    cant_5s=0                                   #numero de palabras de 5 letras
    lista5=[]                                   #Lista de palabras
    with open("palabras5.txt", "w") as g:       #para guardar las palabras en un archivo .txt aparte
        with open("listado.txt", "r", encoding="utf8") as f:
            for line in range (1290):           #lista de palabras de 1290 elementos, cambiar el numero si se cambia la lista
                f_datos = f.readline()
                if len(f_datos) == 6:
                    cant_5s=cant_5s+1
                    g.write(f_datos)            #para guardar las palabras en un archivo .txt aparte
                    lista5.append(f_datos.rstrip())

    #print(">>>OPERACION COMPLETADA CON EXITO")
    #print(">>>SE ENCONTRARON", cant_5s, "PALABRAS DE 5 LETRAS")
    #-----------------------------------------|ETAPA 2|------------------------------------------

    def pregunta(q):                #revisa errores en la palabra introducida
        if q not in lista5:
            print("ERROR:La palabra no está en el diccionario")
            if len(q) != 5:
                print("ERROR:la palabra introducida no es de 5 letras. Por favor vuelva a ingresar una palabra.")
            if not q.isalpha():
                print("ERROR:Contiene caracteres especiales")

    #------------------------------------------|ETAPA 3|------------------------------------------
    devolucion=[]
    #a=solucion
    #B=intento
    def comparador(a,b):            #compara la palabra introducida con la solucion, determina el color de cada letra para la devolucion
        for i in range(5):
            x=a[i]
            y=b[i]
            cantidad_y_i=a.count(y)
            cantidad_y_dev = devolucion.count(Fore.YELLOW+y)+devolucion.count(Fore.GREEN+y)+devolucion.count(y)
            y_restantes=cantidad_y_i-cantidad_y_dev
            if x==y:
                devolucion.append(Fore.GREEN+y)#Verde
                if y_restantes <= 0:
                    sss=devolucion.index(Fore.YELLOW+y) #posicion amrillo
                    devolucion[sss] = Fore.WHITE+y   #reemplaza amarillo
            elif y in a:
                if y_restantes>0:
                    devolucion.append(Fore.YELLOW+y)#Amarillo
                else:
                    devolucion.append(Fore.WHITE+y)#Blanco
            else:
                devolucion.append(Fore.WHITE+y)#Blanco

    def respuesta(m):               #forma la devolucion de la palabra con colores
        qqq="".join(m)
        print("         ",qqq)

    #-------------------------------------------|WORDLE|-------------------------------------------
    print(Back.BLUE+"""----------------Bienvenido a Wordle------------
            Introduzca palabras de 5 letras.   
            No use caracteres especiales.      
            No use mayusculas                  """, Back.RESET)
    intentos=5
    solucion = random.choice(lista5)
    #print("La palabra aleatoria es", solucion)     #borrar el "#" para probar
    palabra=input(Back.CYAN+"Introduzca una palabra:\n"+Back.RESET)
    while intentos>0:
        if palabra!=solucion:
            while palabra not in lista5:
                pregunta(palabra)
                palabra=input(Back.CYAN+"introduzca otra palabra:\n"+Back.RESET)
            comparador(solucion,palabra)
            respuesta(devolucion)
            if palabra!=solucion:
                devolucion=[]
                print(Fore.RED+"le quedan ",str(intentos),"intentos")
                if intentos!=0:
                    palabra=input(Back.CYAN+"Siguiente intento:\n"+Back.RESET)
                intentos=intentos-1
                
        if palabra==solucion:
            print(Back.GREEN+solucion)
            print("¡Ganaste!")
            intentos=0
    print(Back.RED+"Fin del Juego.")
    print("La palabra era:", solucion)