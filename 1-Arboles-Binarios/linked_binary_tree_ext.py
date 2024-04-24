#Implementar la solución aquí
#Integrantes: Aquino, Benjamin - Bravo, Agustin - Cafre Marko
from typing import Any

from data_structures import BinaryTreeNode, LinkedBinaryTree, LinkedList
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract


class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):

  def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
    """ Indica si node1 y node2 son hermanos.

    Args:
      nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
      nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.

    Returns:
      bool: True si los nodos tienen el mismo padre, False en caso contrario.
    """
    #si el arbol esta vacio
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    #si alguno de los nodos es None
    if nodo1 is None or nodo2 is None:
      return False
    else:
      parent = self._search_parent(nodo1)
      parent2 = self._search_parent(nodo2)
      return parent == parent2


  def hojas(self) -> LinkedList:
    """ Devuelve los elementos de los nodos que no tienen ningún hijo.

    Returns:
        LinkedList: lista formada por los elementos de los nodos hoja.
    """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      hojas = LinkedList()
  
      def prueba(nodo):
        if nodo is not None:
          if nodo.children_count() == 0:
            hojas.append(nodo.element)
          prueba(nodo.left_child)
          prueba(nodo.right_child)
      prueba(self._root)
      
    return hojas


  def mayores_que(self, k: Any) -> LinkedList:
    """ Devuelve los elementos de los nodos cuyo valor de clave es mayor que k.

    Args:
      k (Any): valor que se utiliza en el filtrado.

    Returns:
        LinkedList: lista formada por los elementos de los nodos hoja.
    """

    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      res = LinkedList()

      def busqueda(nodo):
        if nodo is not None:
          if nodo.element > k:
            res.append(nodo)
          busqueda(nodo.left_child)
          busqueda(nodo.right_child)

    busqueda(self._root)
    return res
      
