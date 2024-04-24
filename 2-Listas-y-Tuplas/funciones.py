# Indicar integrantes del grupo
# Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

## Programar aquí los ejercicios desde 5 hasta 6 inclusive.

def filtrar_menores(lista, k):
  lista_menores = []
  for i in range(len(lista)):
    if lista[i]<=k:
      lista_menores.append(lista[i])
  return lista_menores

def minimo_maximo(lista):
  tupla = (min(lista), max(lista))
  return tupla