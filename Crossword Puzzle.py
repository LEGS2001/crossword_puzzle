import itertools
from operator import itemgetter

def crosswordPuzzle(crossword, words):
    #Separa las palabras en formato PALABRA;PALABRA a [PALABRA, PALABRA] (Lo hace una lista)
    def separarPalabras(words):
        palabras_lista = words.split(";")
        return palabras_lista

    #Llena el grid
    def separarCasillas(crossword):
        #Agrega las coordenadas de las casillas con - a una lista, separandolas en horizontales y verticales
        casillas_verticales = []
        casillas_horizontales  = []
        for fila in range(10):
            palabra_vertical = []
            palabra_horizontal = []
            for letra in range(10):
                #Recorre las filas del grid y separa las coordenadas de las palabras horizontales
                if crossword[fila][letra] == "-":
                    palabra_horizontal.append([fila, letra])
                elif len(palabra_horizontal) == 1:
                    palabra_horizontal = []
                elif len(palabra_horizontal) >= 2:
                    casillas_horizontales.append(palabra_horizontal)
                    palabra_horizontal = []
                if letra == 9 and len(palabra_horizontal) >= 2:
                    casillas_horizontales.append(palabra_horizontal)
                    palabra_horizontal = []
                #Recorre las columnas del grid y separa las coordenadas de las palabras verticales
                if crossword[letra][fila] == "-":
                    palabra_vertical.append([letra, fila])
                elif len(palabra_vertical) == 1:
                    palabra_vertical = []
                elif len(palabra_vertical) >= 2:
                    casillas_verticales.append(palabra_vertical)
                    palabra_vertical = []
                if letra == 9 and len(palabra_vertical) >= 2:
                    casillas_verticales.append(palabra_vertical)
                    palabra_vertical = []
    
        #Ordena las listas de palabras numericamente para asegurar que pertenezcan a la misma linea/palabra
        casillas_horizontales = sorted(casillas_horizontales, key=itemgetter(0))
        casillas_verticales = sorted(casillas_verticales, key=itemgetter(1))


        #Junta todas las casillas en una sola lista, primero las horizontales, luego las verticales
        casillas_vacias = casillas_horizontales + casillas_verticales

        casillas_vacias_ordenadas = []
        for i in casillas_vacias:
            for j in i:
                casillas_vacias_ordenadas.append(j)
        return casillas_vacias_ordenadas

    #Crea un nuevo grid 10x10 solo con + para rellenarlo 
    def crearNuevoGrid():
        nuevo_grid = []
        for i in range(10):
            nuevo_grid.append([])
            for j in range(10):
                nuevo_grid[i].append("+")
        return nuevo_grid

    solucion = []
    def resolverGrid(nuevo_grid, crossword, palabras):
        global solucion
        solucion = []
        if len(palabras) > 0:
            palabras_unidas = "".join(palabras[0])
            casillas = separarCasillas(crossword)

            #Recorre todas las posiciones de las casillas que tenian -, y si la casilla esta vacia o es la misma letra que toca poner, pone la letra, caso contrario, no hace nada
            for i in range(len(casillas)):
                if nuevo_grid[casillas[i][0]][casillas[i][1]] == "+" or nuevo_grid[casillas[i][0]][casillas[i][1]] == palabras_unidas[0]:
                    nuevo_grid[casillas[i][0]][casillas[i][1]] = palabras_unidas[0]
                    palabras_unidas = palabras_unidas[1:]
                else:
                    continue
            
            #Si se pusieron todas las letras correctamente, devuelve el grid, caso contrario, vuelve a ejecutar la funcion con las palabras en otro orden
            if len(palabras_unidas) > 0:
                palabras.pop(0)
                resolverGrid(crearNuevoGrid(), crossword, palabras)
            else:
                solucion = nuevo_grid
        return solucion

    #Convierte las palabras en una lista
    palabra = separarPalabras(words)

    #Toma la lista de palabras y crea una lista con todas las combinaciones posibles
    palabra = list(itertools.permutations(palabra))

    #Funcion que resuelve el crossword puzzle
    respuesta = resolverGrid(crearNuevoGrid(), crossword, palabra)
    for i in range(len(respuesta)):
        respuesta[i] = "".join(respuesta[i])
    
    print("============")
    print(words)
    for i in crossword:
        print(i)
    print("============")
    for i in respuesta:
        print(i)
    print("============")

#Ejemplos del programa en funcionamiento
crossword = ["+-++++++++",
             "+-++++++++",
             "+-++++++++",
             "+-----++++",
             "+-+++-++++",
             "+-+++-++++",
             "+++++-++++",
             "++------++",
             "+++++-++++",
             "+++++-++++"]
words = "LONDON;DELHI;ICELAND;ANKARA"

crossword2 = ["+-++++++++",
              "+-++++++++",
              "+-------++",
              "+-++++++++",
              "+-++++++++",
              "+------+++",
              "+-+++-++++",
              "+++++-++++",
              "+++++-++++",
              "++++++++++"]
words2 = "AGRA;NORWAY;ENGLAND;GWALIOR"

crossword3 = ["++++++-+++",
              "++------++",
              "++++++-+++",
              "++++++-+++",
              "+++------+",
              "++++++-+-+",
              "++++++-+-+",
              "++++++++-+",
              "++++++++-+",
              "++++++++-+"]
words3 = "ICELAND;MEXICO;PANAMA;ALMATY"

crosswordPuzzle(crossword, words)
crosswordPuzzle(crossword2, words2)
crosswordPuzzle(crossword3, words3)