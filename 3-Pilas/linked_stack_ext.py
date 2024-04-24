#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
# Programar esta clase
from linked_stack_ext_abstract import LinkedStackExtAbstract
from data_structures.linear.stacks.linked_stack import LinkedStack
from typing import Any


class LinkedStackExt(LinkedStack, LinkedStackExtAbstract):

  def multi_pop(self, num: int):  # borre el -> List[Any] porque daba error :)
    """Realiza la cantidad de operaciones pop() indicada por num.
      Args: 
        num (int): número de veces que se va a ejecutar pop().
      Raises: 
        Exception: Arroja excepción si se invoca a pop() por cuando la estructura está vacía.
      Returns:
        List[Any]: lista formada por todos los topes que se quitaron de la pila.
    """
    lista = []

    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      for i in range(0, num):
        lista.append(self.top())
        self.pop()

    return lista

  def replace_all(self, param1: Any, param2: Any) -> None:
    """Reemplaza todas las ocurrencias de param1 en la pila por param2.
      Args:
        param1 (Any): Valor a buscar/reemplazar.
        param2 (Any): Nuevo valor.
    """

    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      nodo = self._head

      while nodo.next:
        if nodo.element == param1:
          nodo.element = param2
        nodo = nodo.next

  def exchange(self) -> None:
    """Intercambia el elemento ubicado en el tope con el más antigüo o último.
        Raises:
          Exception: Arroja excepción si la estructura está vacía.
      """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      nodo_bottom = self._head
      while nodo_bottom.next:
        nodo_bottom = nodo_bottom.next
      nodo_top = self._head
      self.pop()
      self.push(nodo_bottom.element)
      nodo_bottom.element = nodo_top.element
      
