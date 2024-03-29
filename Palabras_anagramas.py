"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.

 Ejemplo de palabra Anagrama => amor y roma
 """

def son_anagramas(palabra1, palabra2):
    #convertir las palabras en minusculas y quitar los espacios
    palabra1 = palabra1.lower().replace(" ","")
    palabra2 = palabra2.lower().replace(" ","")

    #verificar que las palabras tengan la misma longitud
    if len(palabra1) != len(palabra2):
        return False
    
    #poner cada caracter de la palabra en una lista
        #Ejemplo: hola ---> "h", "o", "l", "a"
    lista_palabra1 = list(palabra1)
    lista_palabra2 = list(palabra2)

    #reordenar las listar de manera alfabetica
    lista_palabra1.sort()
    lista_palabra2.sort()

    #Verificar si ambas listas son iguales, si son iguales es porque son anagramas
    if lista_palabra1 == lista_palabra2:
        return True
    else:
        return False

palabra1 = input("Indique una palabra: ")
palabra2 = input("Indique otra palabra: ")

if son_anagramas(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas")
else:
    print(f"{palabra1} y {palabra2} no son anagramas")
