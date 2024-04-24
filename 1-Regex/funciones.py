#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko

import re
from typing import List, Tuple, Dict


def procesar(nombre_archivo: str) -> List[Tuple[str, str]]:
  """Abre el archivo cuyo nombre se pasa por parámetro y
    devuelve una lista de tuplas que tienen como primer elemento
    el tipo de encabezado y como segundo elemento el texto contenido dentro.

    Args:
        nombre_archivo (str): nombre del archivo a procesar

    Returns:
        List[Tuple[str, str]]: Lista de tuplas. 
        Ejemplo: [("h1", "Computación en la nube"), ("h2", "Introducción"), ...].
  """

  with open(nombre_archivo) as file:
    contenido = file.read()

    combinaciones = ["<h1>(.*?)</h1>", "<h2>(.*?)</h2>", "<h3>(.*?)</h3>",
                     "<h4>(.*?)</h4>", "<h5>(.*?)</h5>"]

    res = []

  for k in combinaciones:
    ocurrencias = re.findall(k, contenido)
    for j in ocurrencias:
      tuple = (k[1:3], j)
      res.append(tuple)

  return res


def contar(lista: List[Tuple[str, str]]) -> Dict[str, int]:
  """Cuenta la cantidad de ocurrencias de los encabezados. 

  Args:
      lista (List[Tuple[str, str]]): lista de tuplas (elemento, texto)

  Returns:
      Dict[str, int]: Devuelve un diccionario con los nombres de los 
      elementos como clave y la cantidad de ocurrencias como valor.
  """
  res = {}
  
  for h in lista:
    if h[0] in res:
      res[h[0]] += 1
    else:
      res[h[0]] = 1
  

  return res
