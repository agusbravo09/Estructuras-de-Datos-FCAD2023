# Indicar integrantes del grupo
# Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

# Demostrar el correcto funcionamiento de las funciones aquí.
if __name__ == '__main__':
  import funciones
  
  lista = [5, 8, 21, 45, 25, 11, 2, -29, -3, 31, 39, 72, 22, -6]
  k = int(input("Ingrese el valor de k: "))
  
  print("Lista de elementos menores o iguales a", k, "es", funciones.filtrar_menores(lista, k))
  
  print('*'*50)
  
  print("Tupla:", funciones.minimo_maximo(lista))