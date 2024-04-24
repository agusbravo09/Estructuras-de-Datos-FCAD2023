#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

from typing import List
from abc import ABC, abstractmethod
from calzado import Calzado
from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor


class CalzadoAdminAbstract(ABC):

  def __init__(self) -> None:
    self._lista: List[Calzado] = []

  def agregar(self, item: Calzado) -> None:
    """Agrega al final de self._lista el elemento pasado por parámetro.

        Args:
            item (Calzado): elemento a insertar al final de self._lista.
        """
    self._lista.append(item)

  @abstractmethod
  def __repr__(self) -> str:
    """Transforma todos los elementos de self._lista en un str.

        Returns:
            str: todos los elementos de self._lista concatenados en un único str.
        """
    pass

  @abstractmethod
  def __str__(self) -> str:
    """Transforma todos los elementos de self._lista en un str.

        Returns:
            str: todos los elementos de self._lista concatenados en un único str.
        """
    pass

  @abstractmethod
  def filtrar_por_tipo(self, tipo: CalzadoTipo) -> List[Calzado]:
    """Devuelve una sublista con todos los elementos cuyo tipo coincide con el pasado por parámetro.

        Args:
            tipo (CalzadoTipo): tipo para filtrar.

        Returns:
            List[Calzado]: sublista de calzado cuyo tipo coincide con el parámetro.
        """
    pass

  @abstractmethod
  def filtrar_precio_entre(self,
                           desde: float = 0.00,
                           hasta: float = 0.00) -> List[Calzado]:
    """Devuelve todos los productos cuyo precio se encuentre entre desde y hasta.

        Args:
            desde (float, optional): Importe a partir del cual se quieren los calzados. Si es 0.00 no se tiene en cuenta.
            hasta (float, optional): Importe a partir del cual se quieren los calzados. Si es 0.00 no se tiene en cuenta.
        
        Raises:
            Exception: arroja excepción del tipo ValueError si desde y hasta son 0.00 o si hasta es mayor que desde.

        Returns:
            List[Calzado]: sublista de calzado que cumple con la condición.
        """
    pass

  @abstractmethod
  def cantidad_productos(self) -> int:
    """Devuelve la cantidad de calzados total en stock.

        Returns:
            int: totales de productos teniendo en cuenta el atributo cantidad.
        """
    pass

  @abstractmethod
  def total_productos(self) -> float:
    """Devuelve el importe total de los productos en stock.

        Returns:
            float: total de productos teniendo en cuenta el atributo precio.
        """
    pass
