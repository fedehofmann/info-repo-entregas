# Importo bibliotecas necesarias
import csv

# Esta función me devuelve un diccionario con todos los árboles de un parque específico
def arboles_parque(nombre_archivo, nombre_parque):
    arboles = {}  # Diccionario vacío que va a guardar los árboles del parque indicado

    # Abro el archivo CSV para lectura (modo texto y codificación UTF-8)
    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)  # Leo el archivo como un conjunto de diccionarios

        # Recorro cada fila (cada árbol)
        for fila in lector:
            # Si el árbol está en el parque que busco...
            if fila['espacio_ve'] == nombre_parque:
                id_arbol = fila['id_arbol']  # Tomo el ID del árbol como clave
                arboles[id_arbol] = fila     # Guardo toda la información del árbol (fila)

    return arboles  # Devuelvo el diccionario con los árboles de ese parque


# Esta función me permite reorganizar el dataset completo por parque
# Esto lo necesito porque las preguntas del ejercicio 5 analizan todos los parques juntos

def arboles_por_parque(nombre_archivo):
    parques = {}  # clave: nombre del parque, valor: lista de árboles (diccionarios)

    with open(nombre_archivo, encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            parque = fila['espacio_ve']
            if parque not in parques:
                parques[parque] = []
            parques[parque].append(fila)  # Cada fila es un árbol

    return parques


# 1) El/los parques con más cantidad de árboles
def parques_con_mas_arboles(diccionario):
    lista_tuplas = []

    # Al correr el código me di cuenta que hay un parque llamado S/D que probablemente no pertenezca
    # a ningún espacio verde concreto, así que lo excluyo
    for parque, lista_arboles in diccionario.items():
        if parque != 'S/D':
            lista_tuplas.append((parque, len(lista_arboles)))

    cant_max = 0
    for i in lista_tuplas:
        if i[1] > cant_max:
            cant_max = i[1]

    # Devuelvo una lista con todos los parques que tengan esa cantidad máxima (por si hay empate)
    return [i[0] for i in lista_tuplas if i[1] == cant_max]


# 2) El/los parques con mayor altura promedio
def parques_con_mas_altura(diccionario):
    lista_tuplas = []

    # Recorro cada parque junto con su lista de árboles
    for parque, lista_arboles in diccionario.items():
        cont = 0
        sum = 0

        # Para cada árbol del parque, sumo su altura y llevo un contador
        for x in lista_arboles:
            altura = float(x['altura_tot'])  # Convierto la altura a número por si viene como string
            sum += altura
            cont += 1

        # Calculo el promedio de alturas para ese parque
        promedio = sum / cont

        # Guardo en una tupla el nombre del parque y su altura promedio
        lista_tuplas.append((parque, promedio))

    # Ahora busco la mayor altura promedio entre todos los parques
    alt_max = 0
    for i in lista_tuplas:
        if i[1] > alt_max:
            alt_max = i[1]

    # Guardo todos los parques que tienen esa altura máxima (por si hay empate)
    lista_final = []
    for i in lista_tuplas:
        if i[1] == alt_max:
            lista_final.append(i)

    # Devuelvo solo los nombres de esos parques
    return [i[0] for i in lista_final]


# 3) El/los parques con más variedad de especies (por ID de especie)
def parques_con_mas_variedad_de_especies(diccionario):
    lista_tuplas = []

    for parque, lista_arboles in diccionario.items():
        lista_especies = []
        for i in lista_arboles:
            especie = i['id_especie']
            if especie not in lista_especies:  # Me garantizo contar IDs únicos
                lista_especies.append(especie)
        if parque != 'S/D':
            lista_tuplas.append((parque, len(lista_especies)))

    max_cant = 0
    for i in lista_tuplas:
        if i[1] > max_cant:
            max_cant = i[1]

    return [i[0] for i in lista_tuplas if i[1] == max_cant]


# 4) La especie con más ejemplares en la ciudad
def especie_con_mas_ejemplares(diccionario):
    especies = {}

    # Recorro todos los árboles de todos los parques
    for lista_arboles in diccionario.values():
        for arbol in lista_arboles:
            especie = arbol['nombre_com']  # Tomo el nombre común de la especie

            # Si la especie ya está en el diccionario, le sumo uno; si no, la agrego con valor 1
            if especie in especies:
                especies[especie] += 1
            else:
                especies[especie] = 1

    # Recorro el diccionario y devuelvo aquella especie con mayor cantidad de ejemplares
    cant_max = 0
    for cantidad in especies.values():
        if cantidad > cant_max:
            cant_max = cantidad

    return [especie for especie, cantidad in especies.items() if cantidad == cant_max]


# 5) La razón entre especies exóticas y autóctonas
def razon_exoticas_autoctonas(diccionario):
    exoticas = 0
    autoctonas = 0

    for lista_arboles in diccionario.values():
        for arbol in lista_arboles:
            origen = arbol['origen']
            if origen == 'Exótico':
                exoticas += 1
            elif origen == 'Nativo/Autóctono':
                autoctonas += 1

    # Por las dudas, evito dividir por cero
    if autoctonas == 0:
        return None

    return exoticas / autoctonas