# Crea diccionario con información de un perro
myDog={
    0: "small", #0: clave, llave, atributo
    "name": "Firulais", #name: clave, llave, atributo
    "sex": "male",
    "age": 4,   
}

# Imprime el nombre
print(myDog["name"])
print(myDog[0])

# Modifica el nombre y lo imprime
newName=input('Ingrese el nombre del perro:')
myDog["name"]=newName
print(myDog["name"])

# Crea nuevo elemento en el diccionario
myDog["color"]="white"
print(myDog)

for item in myDog:
    print(f'{item}: {myDog[item]}')

myDog1={
    "name": "Rayita",
    "age": int(input('Ingrese la edad del perro: ')),
    "color": "white",
}

print(myDog1)



