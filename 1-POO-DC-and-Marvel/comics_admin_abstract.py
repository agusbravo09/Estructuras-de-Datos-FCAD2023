#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko

from typing import List, Tuple
from abc import ABC, abstractmethod
from personaje import Personaje
from bando import Bando
from genero import Genero


class ComicsAdminAbstract(ABC):

  def __init__(self) -> None:
    self._lista: List[Personaje] = []

  @abstractmethod
  def agregar_desde_csv(self, ruta: str) -> None:
    """Procesa el archivo CSV cuya ruta se pasa por parámetro y agrega cada uno de los personajes
        a self._lista como una instancia de la clase Personaje

        Args:
            ruta (str): dirección absoluta o relativa hacia el archivo.
        """

  def agregar(self, personaje: Personaje) -> None:
    self._lista.append(personaje)

  @abstractmethod
  def __str__(self) -> str:
    """Concatena en un único str todos los personajes de self._lista.

        Returns:
            #str: cadena con todos los personajes de self._lista
        """

  @abstractmethod
  def filtrar_por_bando(self,
                        bando: Bando,
                        limite: int = 0) -> List[Personaje]:
    """Devuelve los personajes cuyo bando coincide con el parámetro bando.

        Args:
            bando (Bando): valor para aplicar el filtro.
            limite (int, optional): cuando es mayor que 0 (cero) indica la cantidad de
            resultados a devolver. Valor por defecto 0.

        Returns:
            List[Personaje]: _description_
       """

  @abstractmethod
  def filtrar_por_genero(self,
                         genero: Genero,
                         limite: int = 0) -> List[Personaje]:
    """Retorna una sublista formada por los personajes cuyo género coincide con 
        el pasado por parámetro.

        Args:
            genero (Genero): se aplica al filtro
            limite (int, optional): cuando es mayor que 0 (cero) indica la cantidad de
            resultados a devolver. Valor por defecto 0

        Returns:
            List[Personaje]: Sublista de personajes con género igual al parámetro genero.
        """
    pass

  @abstractmethod
  def contar_por_universo(self) -> Tuple[int, int]:
    """Cuenta la cantidad de personajes de cada universo y retorna una tupla de dos posiciones.
        La posición 0 de la tupla con la cantidad de personajes de DC y
        La posición 1 de la tupla con la cantidad de personajes de Marvel

        Returns:
            Tuple[int, int]: Tupla de enteros formada por la cantidad de personajes de cada universo.
        """
