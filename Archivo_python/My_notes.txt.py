
direccion = "my_notes.txt"
file = open(direccion, 'r')
print(file)

print("___________________________________________")

lineas = file.readlines()
print(lineas)

for l in lineas:
    print(l.replace('\n', ''))

file.close()

with open('my_notes.txt', 'r') as archivo:
    argumento = archivo.read()
    lineas = argumento.split('\n')
    print(lineas)



