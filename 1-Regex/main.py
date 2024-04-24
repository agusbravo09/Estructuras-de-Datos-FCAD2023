#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko

from funciones import procesar, contar

# No remover esta línea el condicional de ejecución.
if __name__ == '__main__':

  # Proceso el archivo
  lista = procesar("cloud.html")

  # Muestro la lista de resultados
  print("Lista resultados: ", *lista, sep="\n")

  # Cuento la cantidad de ocurrencias.
  print("Cantidad de encabezados: ", contar(lista))
