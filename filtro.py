with open("palabras5.txt", "w") as g:
    with open("listado.txt", "r") as f:
        for line in f:
            f_datos = f.readline()
            #print(f.readline)
            if len(f_datos) == 6:
                print("5")
                g.write(f_datos)
print("hecho")