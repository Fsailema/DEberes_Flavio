
# Diccionario
#ingresamaos la clave_valor
informacion_personal = {"nombre":"Juan","edad":"20","ciudad":"Puyo","profesion":"cocinero"}

#modidfiocamos la clave "cuidad" por otra
informacion_personal["ciudad"] = "Ambato"

#buscamos la clave "telefono" y como no existe agregamos al diccionario
informacion_personal["telefono"] = "0997788123"

#eliminamos la clave "edad" ya que no es muy importante
del(informacion_personal["edad"])

print(informacion_personal)

