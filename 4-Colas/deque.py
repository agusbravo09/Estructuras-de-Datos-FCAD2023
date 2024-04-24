#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
#Programar esta clase
from deque_abstract import DequeAbstract
from typing import Any, Optional
from data_structures.linear.list_node import ListNode


class Deque(DequeAbstract):

  def __init__(self) -> None:
    self._front: Optional[ListNode] = None
    self._back: Optional[ListNode] = None
    self._size: int = 0

  def __len__(self) -> int:
    """  Devuelve la cantidad actual de elementos en la estructura.
        Returns:
          int: Devuelve la cantidad de elementos, cero la si estructura está vacía.
    """
    return self._size

  def __str__(self) -> str:
    """ Concatena en un único string todos los elementos almacenados 
        en los nodos de la estructura.

        Returns:
            str: convierte en str todos los elementos y los concatena en un string.
        """

    #Si la estructura está vacía => retorno siempre lo mismo.
    if self.is_empty():
      return "LinkedQueue()"

    resultado = ""  # inicializo resultado con el string vacío

    #Me quedo en actual con el elemento ubicado en el frente
    actual = self._front
    while actual:
      # proceso el elemento del nodo actual
      resultado += str(actual.element) + ", "

      # establezco el siguiente nodo como nodo actual
      actual = actual.next

    #Quito los dos últimos caracteres del string
    resultado = resultado[:len(resultado) - 2]

    return f"LinkedQueue({resultado})"

  def is_empty(self) -> bool:
    """Indica si la estructura está vacía.

        Returns:
            bool: True si la estructura está vacía, False en caso contrario.
        """
    return self._size == 0

  def first(self) -> Any:
    """Devuelve el elemento ubicado en el frente de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía.

        Returns:
            Any: Devuelve el elemento dato correspondiente al frente de la estructura.
        """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      return self._front.element

  def last(self) -> Any:
    """ Devuelve el elemento correspondiente al nodo ubicado al final de
        la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía.

        Returns:
            Any: Devuelve el elemento dato correspondiente al final de la estructura.
        """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      self._back = self._front
      while self._back.next:
        self._back = self._back.next
      return self._back.element

  def add_first(self, element: Any) -> None:
    """_summary_

        Args:
            element (Any): elemento que va a ser agregado al principio de la estructura.
        """
    nodo = ListNode(element)

    if self.is_empty():
      self._front = nodo
    else:
      nodo.next = self._front
      self._front = nodo

    self._size += 1

  def add_last(self, element: Any) -> None:
    """Agrega un elemento al final de la estructura.

        Args:
            element (Any): elemento que va a ser agregado al final de la estructura.
        """
    nodo_nuevo = ListNode(element)
    if self.is_empty():
      self._front = nodo
    else:
      self._back = self._front
      while self._back.next:
        self._back = self._back.next
          
      self._back.next = nodo_nuevo
        


    self._size += 1

  def delete_first(self) -> None:
    """Quita el elemento ubicado en el frente de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía.
        """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      self._front = self._front.next
      self._size -= 1 

  def delete_last(self) -> None:
    """Quita el elemento ubicado al final de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está vacía.
        """
    if self.is_empty():
      raise Exception("La estructura esta vacia")
    else:
      self._back = self._front
      while self._back.next:
        previous = self._back
        self._back = self._back.next

      previous.next = None
      self._size -= 1
      
