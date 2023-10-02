#creamos el archivo
direccion = "my_notes.txt"

#abrimos el archivo
file = open(direccion, 'r')
print(file)

print("___________________________________________")
#para leer el archivo linea por linea
lineas = file.readline()
print(lineas)
lineas = file.readline()
print(lineas)
lineas = file.readline()
print(lineas)

file.close()

#para leer como una lista

with open('my_notes.txt', 'r') as archivo:
    argumento = archivo.read()
    lineas = argumento.split('\n')
    print(lineas)

#para leer todo sin el espacio

for l in lineas:
    print(l.replace('\n', ''))

file.close()

#para escribir un archivo nuevo desde python

contenido = "fútbol, películas, pasear"
nueva_ruta = "my_notes.txt2"
file = open(nueva_ruta, 'w')
file.write(contenido)

file.close()
