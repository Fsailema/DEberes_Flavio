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


