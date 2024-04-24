#Integrantes: Aquino, Benjamin - Bravo, Agustin - Cafre Marko

from data_structures import BinaryTreeNode
from linked_binary_tree_ext import LinkedBinaryTreeExt


def main():
  nodo_a = BinaryTreeNode('A')
  nodo_b = BinaryTreeNode('B')
  nodo_c = BinaryTreeNode('C')
  nodo_d = BinaryTreeNode('D')
  nodo_f = BinaryTreeNode('F')
  nodo_g = BinaryTreeNode('G')
  nodo_h = BinaryTreeNode('H')
  nodo_i = BinaryTreeNode('I')
  nodo_k = BinaryTreeNode('K')
  nodo_m = BinaryTreeNode('M')
  nodo_n = BinaryTreeNode('N')

  arbol = LinkedBinaryTreeExt()
  arbol.add_left_child(None, nodo_a)

  arbol.add_left_child(nodo_a, nodo_b)
  arbol.add_right_child(nodo_a, nodo_f)

  arbol.add_left_child(nodo_b, nodo_c)
  arbol.add_right_child(nodo_b, nodo_d)

  arbol.add_left_child(nodo_f, nodo_g)
  arbol.add_right_child(nodo_f, nodo_k)

  arbol.add_left_child(nodo_g, nodo_h)
  arbol.add_right_child(nodo_g, nodo_i)

  arbol.add_left_child(nodo_k, nodo_m)
  arbol.add_right_child(nodo_k, nodo_n)

  print(arbol)

  print("Metodo Hermanos (nodo n con nodo a)")
  print(arbol.hermanos(nodo_n, nodo_a))
  
  print("*"*50)

  print("Metodo Hojas")
  print(arbol.hojas())

  print("*"*50)

  print("Metodo Mayores que")
  print(arbol.mayores_que("M"))

if __name__ == '__main__':
  main()
