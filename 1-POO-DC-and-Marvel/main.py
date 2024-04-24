#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko

from comics_admin import ComicsAdmin
from bando import Bando
from genero import Genero

try:
  comics = ComicsAdmin()
  comics.agregar_desde_csv("marvel_dc_characters.csv")

  print("**********")
  print("**********")
  print("  Buenos  ")
  print("**********")
  print("**********")
  print(comics.filtrar_por_bando(bando=Bando.GOOD, limite=5))

  print("**********")
  print("**********")
  print("  Malos  ")
  print("**********")
  print("**********")
  print(comics.filtrar_por_bando(bando=Bando.BAD, limite=5))

  print("**********")
  print("**********")
  print(" Femenino ")
  print("**********")
  print("**********")
  print(comics.filtrar_por_genero(genero=Genero.FEMALE, limite=5))

  print("**********")
  print("**********")
  print(" Universo ")
  print("**********")
  print("**********")
  print(comics.contar_por_universo())

except Exception as exc:
  print(exc)
