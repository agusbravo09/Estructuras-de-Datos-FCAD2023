#Integrantes: Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

from array_heap_ext import ArrayHeapExt
from data_structures.priority_queues import array_heap


def main():
  # Implementar el cliente en esta función.
  array_heap = ArrayHeapExt()
  array_heap2 = ArrayHeapExt()

  array_heap2.add(5, 'x')
  array_heap2.add(9, 'F')
  array_heap2.add(12, 'L')
  array_heap2.add(22, 'T')

  array_heap.add(2, 'A')
  array_heap.add(4, 'B')
  array_heap.add(6, 'C')
  array_heap.add(1, 'D')

  print("ArrayHeap 1")
  print(array_heap)

  print("*" * 60)

  print("ArrayHeap 2")
  print(array_heap2)

  print("*" * 60)

  print("metodo eliminar por prioridad - k = 2 (modifica ArrayHeap 1)")
  array_heap.eliminar_por_prioridad(2)
  print(array_heap)

  print("*" * 60)

  print(
      "Metodo cambiar prioridad - k_actual: 1, k_nuevo: 100 (modifica ArrayHeap 1)"
  )
  array_heap.cambiar_prioridad(1, 100)
  print(array_heap)

  print("*" * 60)

  print("Metodo fusionar")
  array_heap.fusionar(array_heap2)
  print(array_heap)

  print("*" * 60)

  print("Metodo vaciar")
  array_heap.vaciar()
  print(array_heap)

  print("*" * 60)


if __name__ == '__main__':
  main()
