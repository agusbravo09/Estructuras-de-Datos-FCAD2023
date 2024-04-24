#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
# No remover esta línea el condicional de ejecución.
from deque import Deque

def main():
  cola = Deque()

  cola.add_first(1)
  cola.add_first(2)
  cola.add_first(3)

  cola.add_last(9)
  cola.add_last(90)
  cola.add_last(123)
  print(cola)

  print("Metodo Len")
  print(cola.__len__())
  print("-"*50)

  print("Metodo STR")
  print(cola)
  print("-"*50)

  print("Metodo Is Empty (deberia mostrar false)")
  print(cola.is_empty())
  print("-"*50)

  print("Metodo Add First - agregaria 10")
  cola.add_first(10)
  print(cola)
  print("-"*50)

  print("Metodo Add Last - agregaria 20")
  cola.add_last(20)
  print(cola)
  print("-"*50)

  print("Metodo Delete First - eliminaria 10")
  cola.delete_first()
  print(cola)
  print("-"*50)

  print("Metodo Delete Last - eliminaria 20")
  cola.delete_last()
  print(cola)
  print("-"*50)

  print("Metodo First")
  print(cola.first())
  print("-"*50)

  print("Metodo Last")
  print(cola.last())
  print("-"*50)


  
if __name__ == '__main__':
  main()
