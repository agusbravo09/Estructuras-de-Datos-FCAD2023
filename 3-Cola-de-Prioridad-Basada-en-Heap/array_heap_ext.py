#Implementar la solución aquí
#Integrantes: Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

from typing import Any
from data_structures import ArrayHeap
from array_heap_ext_abstract import ArrayHeapExtAbstract


class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):

  def fusionar(self, otro: ArrayHeap) -> None:
    """Combina los elementos de otro heap en este dejándolos perfectamente ordenados.

    Args:
        otro (ArrayHeap): ArrayHeap pasado por parámetro.
    """
    if not isinstance(otro, ArrayHeap):
      raise Exception("El parametro ingresado debe ser de tipo ArrayHeap")
    if self.is_empty():
      self._data = otro._data
    if otro.is_empty():
      return
    else:
      for items in otro._data:
        self.add(items._key, items._value)

  def vaciar(self) -> None:
    """ Una vez invocado el Heap queda sin elementos. """
    while self._data:
      self._data.pop()

  def eliminar_por_prioridad(self, k: Any) -> None:
    """ Elimina el elemento con prioridad igual al parámetro k.
    Luego de ser invocado la estructura debe preservar la condición de orden

    Args:
        k (Any): prioridad del elemento a eliminar.
    """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    else:
      for i in range(0, self._data.__len__()):
        if self._data[i]._key == k:
          self._data.pop(i)
          break

          
          
  
  def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
    """ Cambia la prioridad de los nodos con prioridad igual k_actual y establece como nueva prioridad k_nueva.

    Args:
      k_actual (Any): prioridad actual del elemento a modificar
      k_nueva (Any): nueva prioridad que debe ser asignada.
    """
    if self.is_empty():
      raise Exception("La estructura esta vacia.")
    for elem in self._data:
      if elem._key == k_actual:
        elem._key = k_nueva

