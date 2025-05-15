# Ejercicio 1
def invertir_lista (lista):
  lista_2 = []
  for i in range (1, len(lista) + 1):
    lista_2.append(lista[-i])
  return lista_2

# Ejercicio 2 - Quiero que devuelva la cantidad de pasos, tengo que pensar en cantidad de pasos
def collatz (nro):
  if nro == 1:
    return 0 # Llegar al 1 no cuenta como un paso
  else:
      if nro % 2 == 0:
        valor = nro // 2
      else:
        valor = nro * 3 + 1
      return 1 + collatz(valor) # Cada llamada recursiva implica un nuevo paso, a menos que llegue al 1 y me va a retornar 0
  
# Ejercicio 2 - Se me ocurrió que es mucho más fácil usando un while
def collatz_2 (nro):
    cont = 0 # El contador arranca en -
    while nro != 1: # El ciclo se va a repetir hasta que el número sea igual a 1
        if nro % 2 == 0:
          nro = nro // 2
        else:
          nro = nro * 3 + 1
        cont += 1 # Sumo un paso al contador
    return cont

# Ejercicio 3 a)
def contar_definiciones(d):
    resultado = {}
    for i in d:  # i es la clave del diccionario (ej: "Federico", "Santiago")
        cont = len(d[i])  # d[i] es la lista de definiciones asociada a esa clave
        resultado[i] = cont  # Guardo la cantidad de definiciones para esa clave
    return resultado

# Ejercicio 3 b)
def cantidad_de_claves_letra (d, l):
  cantidad = 0
  for i in d: # i es la clave del diccionario (ej: "Federico", "Santiago")
    for x in i: # x va a recorrer el string clave
      if x[0] == l: # Le pido que la primera letra de cada string sea igual a l
        cantidad += 1
  return cantidad

# Ejercicio 4
def propagar(l):
    # Propago hacia la derecha
    for i in range(0, len(l)):  # Recorro toda la lista
      if l[i] == 1:  # Si encuentro un fósforo encendido
        for x in range(i + 1, len(l)):  # Recorro desde una posición más adelante de la lista porque necesito comparar con el que tiene adelante
            if l[x] == -1:  # Si encuentro un fósforo negro freno
                break
            if l[x] == 0:  # Si encuentro un fósforo rojo lo enciendo
                l[x] = 1
    # Propago hacia la izquierda (misma lógica pero barriendo la lista de atrás hacia adelante)
    for i in range (len(l)-1, -1, -1):
      if l[i] == 1:
        for x in range (len(l)- 1- i, -1, -1):
          if l[x] == -1:
            break
          if l[x] == 0:
            l[x] = 1
    return l