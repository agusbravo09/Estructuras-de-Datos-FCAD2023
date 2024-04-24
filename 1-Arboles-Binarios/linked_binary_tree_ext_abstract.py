from abc import ABC, abstractmethod
from typing import Any
from data_structures import LinkedList, BinaryTreeNode


class LinkedBinaryTreeExtAbstract(ABC):
  """ Conjunto de métodos adicionales a LinkedBinaryTree"""

  @abstractmethod
  def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
    """ Indica si node1 y node2 son hermanos.

    Args:
      nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
      nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.

    Returns:
      bool: True si los nodos tienen el mismo padre, False en caso contrario.
    """
    pass

  @abstractmethod
  def hojas(self) -> LinkedList:
    """ Devuelve los elementos de los nodos que no tienen ningún hijo.

    Returns:
        LinkedList: lista formada por los elementos de los nodos hoja.
    """
    pass

  @abstractmethod
  def mayores_que(self, k: Any) -> LinkedList:
    """ Devuelve los elementos de los nodos cuyo valor de clave es mayor que k.

    Args:
      k (Any): valor que se utiliza en el filtrado.

    Returns:
        LinkedList: lista formada por los elementos de los nodos hoja.
    """
    pass
