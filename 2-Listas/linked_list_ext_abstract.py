#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
from abc import ABC, abstractmethod
from typing import Any


class LinkedListExtAbstract(ABC):

  @abstractmethod
  def add_first(self, elem: Any) -> None:
    """Agrega un elemento al principio de la estructura"""
    pass

  @abstractmethod
  def pop(self) -> None:
    """ Quita el último elemento de la lista."""
    pass

  @abstractmethod
  def reverse(self) -> None:
    """ Invierte el orden de los elementos en la lista utilizando un enfoque recursivo.
    """
    pass
