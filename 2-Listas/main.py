#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
# No remover esta línea el condicional de ejecución.
from linked_list_ext import LinkedListExt


def main():
  lista = LinkedListExt()
  lista.append(1)
  lista.append(2)
  lista.append(3)
  

  print("Metodo Add First")
  lista.add_first(4)
  lista.add_first(7)
  lista.add_first(10)
  
  print(lista)
  print("*"*50)
  
  
  print("Metodo Pop")

  lista.pop()
  print(lista)
  print("*"*50)

  print("Metodo Reverse")
  lista.reverse()
  print(lista)
  print("*"*50)
  

if __name__ == '__main__':
  main()
