#Integrantes: Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

from unsorted_priority_queue import UnsortedPriorityQueue


def main():

  priority_queue = UnsortedPriorityQueue()

  priority_queue.add(2, "A")
  priority_queue.add(5, "B")
  priority_queue.add(59, "D")
  priority_queue.add(1, "X")
  priority_queue.add(30, "E")

  print("Metodo __str__")
  print(priority_queue)

  print(" ")

  print("Metodo __len__")
  print(priority_queue.__len__())

  print(" ")

  print("Metodo is_empty"
        )  # deberia imprimir true si la estructura esta vacia, sino false
  print(priority_queue.is_empty())

  print(" ")

  print("Metodo min")
  print(priority_queue.min())

  print(" ")

  print("Metodo remove_min")
  print("Se ha removido: ", priority_queue.remove_min())
  print(priority_queue)


if __name__ == '__main__':
  main()
