# Importo librerías
import random
import numpy as np
import pandas
import matplotlib.pyplot as plt

# Implemento la función crear_album(figus_total) que devuelve un álbum (vector/lista) vacío con figus_total espacios para pegar figuritas
def crear_album(figus_total):
  album = []
  for i in range (0, figus_total):
    album.append(0)
  return album

# Implemento la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False si está completo
def album_incompleto(A):
  if 0 in A:
    return True
  else:
    return False
  
  # Implemento una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó
def comprar_figus (figus_total):
  figurita_nueva = random.randint(0, figus_total - 1) # Tengo que pensar en posiciones de mi lista (album), por lo que debe ir de 0 a 859 (en mi ejemplo)
  return figurita_nueva

# Implemento una función cuantas_figus(figus_total) que dado el tamaño del álbum:
# 1. Genere un álbum nuevo
# 2. Simule su llenado
# 3. Devuelva cuántas figuritas se debieron comprar para completarlo
def cuantas_figus(figus_total):
  album = crear_album(figus_total) # Creo el album con el que voy a simular el llenado
  while album_incompleto(album) == True:
    figurita_nueva = comprar_figus(figus_total)
    album[figurita_nueva] += 1
  return sum(album)

# Escribo una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado de n_repeticiones álbums de figus_total figuritas y devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el álbum
def experimento_figus(n_repeticiones, figus_total):
  n_reps = 0 # Arranco desde cero, asi que el ciclo debe tener MENOS de n_repeticiones, CUIDADO CON ESTO
  lista_resultados = [] # Lista de resultados
  while n_reps < n_repeticiones: # Ciclo para simular las repeticiones
    lista_resultados.append(cuantas_figus(figus_total)) # Acá es donde invoco a la función y le paso el número 6 como parámetro
    n_reps += 1
  avg_resultados = sum(lista_resultados) / len(lista_resultados)
  return avg_resultados

# Implemento una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar
def comprar_paquete(figus_total, figus_paquete):
  paquete = []
  n_paquete = 0
  while n_paquete < figus_paquete: # Como arranco en 0 tiene que ser MENOR a la cantidad de figuritas (en mi ejemplo menor a 5)
    paquete.append(random.randint(0, figus_total - 1)) # Tengo que pensar en posiciones de mi lista (album), por lo que debe ir de 0 a 859 (en mi ejemplo)
    n_paquete += 1
  return paquete

# Implemento una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete:
# 1. Genere un álbum nuevo
# 2. Simule su llenado
# 3. Devuelva cuántos paquetes se debieron comprar para completarlo
def cuantos_paquetes(figus_total, figus_paquete):
  album = crear_album(figus_total)
  n_paquetes = 0
  while album_incompleto(album) == True:
    paquete = comprar_paquete(figus_total, figus_paquete)
    for i in paquete:
      album[i] += 1
    n_paquetes += 1
  return n_paquetes

# Código de pruebas opcionales
if __name__ == "__main__":
  # Ejecuto n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardo en una lista los resultados obtenidos en cada repetición
  # Con los resultados obtenidos estimo cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas
  n = 0 # Arranco desde cero, asi que el ciclo debe tener MENOS de 1000 repeticiones, CUIDADO CON ESTO
  lista_resultados_6 = [] # Lista de resultados
  while n < 1000: # Ciclo para simular las repeticiones
    lista_resultados_6.append(cuantas_figus(6)) # Acá es donde invoco a la función y le paso el número 6 como parámetro
    n += 1
  avg_resultados_6 = sum(lista_resultados_6) / len(lista_resultados_6)
  print(avg_resultados_6)

  # Calculo n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860 y figus_paquete = 5
  # Guardo los resultados obtenidos en una lista y calculo su promedio
  # Si los recursos de la computadora lo permiten, lo hago con 1000 repeticiones
  lista_resultados = []
  n = 0
  while n < 1000: # Acá configuro la cantidad de iteraciones
    lista_resultados.append(cuantos_paquetes(860, 5))
    n += 1
  promedio_resultados = sum(lista_resultados) / len(lista_resultados)
  print(promedio_resultados)