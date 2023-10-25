#1. Función que recibe un diccionario y agrega una clave-valor, retorna el diccionario actualizado
def agregarAlDict(diccionario: dict, clave, valor):    
    diccionario.update({clave:valor})

    return diccionario

#2. Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
def eliminarDeDict(diccionario: dict, clave):
    diccionario.pop(clave)
    return diccionario

#3. Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo
def modificarDelDict(diccionario: dict, clave, valor):
    if (diccionario.get(clave) == None):
        return False
    else:
        diccionario.update({clave:valor})
        return True    

#4. Función que combine dos diccionarios, regresar el diccionario resultante
def combinarDiccionarios(diccionario1: dict, diccionario2: dict):
    resultado = diccionario1.update(diccionario2)
    return resultado

#5. Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
def agregarAlSet(conjunto: set, elemento):
    if elemento in conjunto:
        return False
    else:    
        conjunto.add(elemento)
        return True
    
#6. Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo
def eliminarDelSet(conjunto: set, elemento):
    if elemento not in conjunto:
        return False
    else:
        conjunto.remove(elemento)
        return True

#7. Función que combine dos conjuntos, regresar el conjunto resultante
def combinarSets(conjunto1: set, conjunto2: set):
    resultado = conjunto1.union(conjunto2)
    return resultado
#8. función que regrese la diferencia de dos conjuntos
def diferenciasEnSets(conjunto1: set, conjunto2: set):
    resultado = conjunto1.symmetric_difference(conjunto2)
    return resultado

#9. Función que elimine un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def eliminarElementoTupla(tupla: tuple, elemento):
    if elemento in tupla:
        nuevo = list(tupla)
        nuevo.remove(elemento)
        resultado = tuple(nuevo)
        return resultado
    else:
        return tupla

#10. Función que concatene dos tuplas en una nueva, regresar la nueva tupla
def concatenarTuplas(tupla1: tuple, tupla2: tuple):
    resultado = list(tupla1) + list(tupla2)
    return tuple(resultado)

#11. Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def invertirTupla(tupla: tuple):
    resultado = list(tupla)
    resultado.reverse()
    return tuple(resultado)


#12. Función que recibe un diccionario y lo imprime
def imprimirDiccionario(diccionario):
    if isinstance(diccionario, dict):
        print(diccionario)
    else:
        print("No es un diccionario...")
    
#13. Función que recibe un tupla y la imprime
def imprimirTupla(tupla):
    if isinstance(tupla, tuple):
        print(tupla)
    else:
        print("No es una tupla...")
#14. Función que recibe un conjunto y lo imprime
def imprimirSet(conjunto):
    if isinstance(conjunto, set):
        print(conjunto)
    else:
        print("No es un conjunto...")



# Código de prueba
diccionarioEjemplo1 = {"A":253, "B":53}
diccionarioEjemplo2 = {"C":53, "D":73}
tuplaEjemplo1 = ("elemento1", "elemento2", "elemento3")
tuplaEjemplo2 = ("elemento4", "elemento5", "elemento6")
setEjemplo1 = {"x1", "x2", "x3"}
setEjemplo2 = {"x4", "x5", "x6"}

print("Función 1: ")
print(diccionarioEjemplo1)
agregarAlDict(diccionarioEjemplo1, "G", 6321)
print(diccionarioEjemplo1)

print("")

print("Función 2: ")
print(diccionarioEjemplo1)
eliminarDeDict(diccionarioEjemplo1, "A")
print(diccionarioEjemplo1)

print("")

print("Función 3: ")
print(diccionarioEjemplo2)
modificarDelDict(diccionarioEjemplo2, "D", 7764)
print(diccionarioEjemplo2)

print("")

print("Función 4: ")
print(diccionarioEjemplo1)
print(diccionarioEjemplo2)
combinarDiccionarios(diccionarioEjemplo1,diccionarioEjemplo2)
print(diccionarioEjemplo1)

print("")

print("Función 5: ")
print(setEjemplo2)
agregarAlSet(setEjemplo2, "x2")
print(setEjemplo2)

print("")

print("Función 6: ")
print(setEjemplo1)
eliminarDelSet(setEjemplo1, "x3")
print(setEjemplo1)

print("")

print("Función 7: ")
print(setEjemplo1)
print(setEjemplo2)
print(combinarSets(setEjemplo1, setEjemplo2))

print("")

print("Función 8: ")
print(setEjemplo1)
print(setEjemplo2)
print(diferenciasEnSets(setEjemplo1, setEjemplo2))

print("")

print("Función 9: ")
print(tuplaEjemplo1)
print(eliminarElementoTupla(tuplaEjemplo1, "elemento2"))

print("")

print("Función 10: ")
print(tuplaEjemplo1)
print(tuplaEjemplo2)
print(concatenarTuplas(tuplaEjemplo1, tuplaEjemplo2))

print("")

print("Función 11: ")
print(tuplaEjemplo1)
print(invertirTupla(tuplaEjemplo1))

print("")

print("Función 12: ")
imprimirDiccionario(diccionarioEjemplo1)

print("")

print("Función 13: ")
imprimirTupla(tuplaEjemplo1)

print("")

print("Función 14: ")
imprimirSet(setEjemplo1)