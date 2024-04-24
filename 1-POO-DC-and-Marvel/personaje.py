#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko

from bando import Bando
from genero import Genero
from universo import Universo


class Personaje:

  def __init__(self, id: int, nombre: str, bando: Bando, genero: Genero,
               universo: Universo) -> None:
    self.id = id
    self.nombre = nombre
    self.bando = bando
    self.genero = genero
    self.universo = universo

  def __eq__(self, other) -> bool:
    if not isinstance(other, Personaje):
      return False
    return self.id == other.id and self.nombre == other.nombre  #el id es unico

  def __str__(self) -> str:
    return repr(self)

  def __repr__(self) -> str:
    return f"Personaje: ID: {self.id} Nombre: {self.nombre} {self.bando} {self.genero} {self.universo} \n"
