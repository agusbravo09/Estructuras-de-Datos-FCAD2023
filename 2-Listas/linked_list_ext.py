#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
# Programar esta clase
from typing import Any

from data_structures import LinkedList
from data_structures.linear.list_node import ListNode
from linked_list_ext_abstract import LinkedListExtAbstract


class LinkedListExt(LinkedList, LinkedListExtAbstract):

  def add_first(self, elem: Any) -> None:
    """Agrega un elemento al principio de la estructura"""
    nodo = ListNode(elem)

    if self.is_empty():
      self._header.next = nodo
    else:
      nodo.next = self._header.next
      self._header.next = nodo

    self._size += 1

  def pop(self) -> None:
    """ Quita el último elemento de la lista."""
    
    if self.is_empty():
      raise Exception("La lista esta vacia")
    else:
      actual = self._header
      while actual.next:
        previo = actual
        actual = actual.next
        
      previo.next = None
      self._size -= 1

  def reverse(self) -> None:
    """ Invierte el orden de los elementos en la lista utilizando un enfoque recursivo.
    """
    lista_Auxiliar = LinkedList()
    if self.is_empty():
      pass
    else:
      actual = self._header
      while actual.next:
        previo = actual
        actual = actual.next

      previo.next = None
      self._size -= 1
      self.reverse()
      self.add_first(actual.element)
      
      
