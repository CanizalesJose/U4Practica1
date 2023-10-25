#1. Función que recibe un diccionario y agrega una clave-valor, retorna el diccionario actualizado
def agregarElemento(diccionario, clave, valor):    
    diccionario.update({clave:valor})

    return diccionario

#2. Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
def eliminarElemento(diccionario, clave):
    diccionario.pop(clave)
    return diccionario

#3. Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo
def modificarElemento(diccionario, clave, valor):
    if (diccionario.get(clave) == None):
        return False
    else:
        diccionario.update({clave:valor})
        return True    

#4. Función que combine dos diccionarios, regresar el diccionario resultante
def combinarDiccionarios(diccionario1, diccionario2):
    resultado = diccionario1.update(diccionario2)
    return resultado

#5. Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
def agregarAlSet(conjunto, elemento):
    if elemento in conjunto:
        return False
    else:    
        conjunto.add(elemento)
        return True
    
#6. Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo
def eliminarDelSet(conjunto, elemento):
    if elemento not in conjunto:
        return False
    else:
        conjunto.remove(elemento)
        return True

#7. Función que combine dos conjuntos, regresar el conjunto resultante
def combinarSets(conjunto1, conjunto2):
    resultado = conjunto1.union(conjunto2)
    return resultado
#8. función que regrese la diferencia de dos conjuntos
def diferenciasEnSets(referencia, comparado):
    resultado = referencia.symmetric_difference(comparado)
    return resultado

#9. Función que elimine un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def eliminarElementoTupla(tupla, elemento):
    if elemento in tupla:
        nuevo = list(tupla)
        nuevo.remove(elemento)
        resultado = tuple(nuevo)
        return resultado
    else:
        return tupla

#10. Función que concatene dos tuplas en una nueva, regresar la nueva tupla
def concatenarTuplas(tupla1, tupla2):
    resultado = list(tupla1) + list(tupla2)
    return tuple(resultado)

#11. Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def invertirTupla(tupla):
    resultado = list(tupla)
    resultado.reverse()
    return tuple(resultado)


#12. Función que recibe un diccionario y lo imprime
def imprimirDiccionario(diccionario):
    try:
        dict(diccionario)
        print(diccionario)
    except:
        
        return
#13. Función que recibe un tupla y la imprime
#14. Función que recibe un conjunto y lo imprime




# Código de prueba
diccionarioEjemplo1 = {"A":253, "B":53}
diccionarioEjemplo2 = {"C":53, "D":73}
tuplaEjemplo1 = ("elemento1", "elemento2", "elemento3")
tuplaEjemplo2 = ("elemento4", "elemento5", "elemento6")

imprimirDiccionario(tuplaEjemplo1)
