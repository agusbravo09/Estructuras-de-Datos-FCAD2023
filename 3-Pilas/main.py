#Integrantes: Bravo, Agustin - Aquino, Benjamin - Cafre, Marko
# No remover esta línea el condicional de ejecución.
from linked_stack_ext import LinkedStackExt

def main():
  pila = LinkedStackExt()

  pila.push(1)
  pila.push(2)
  pila.push(3)

  print("*"*50)
  print("Metodo Multi Pop")
  print("Pila Original: ", pila)
  print("Topes que se quitaron de la pila: ", pila.multi_pop(2))
  print("After Multipop: ", pila)
  print("*"*50)

  pila.push("hola")
  pila.push("mundo")
  pila.push("adios")
  pila.push("hola")

  print("*"*50)
  print("Metodo Replace All")
  print("Pila Original: ", pila)
  pila.replace_all("hola", 240)
  print("Pila reemplazada: ", pila)
  print("*"*50)

  pila2 = LinkedStackExt()

  pila2.push("Entre Rios")
  pila2.push("Cordoba")
  pila2.push("Buenos Aires")
  pila2.push("La Rioja")
  
  print("*"*50)
  print("Metodo Exchange")
  print("Pila Original: ", pila2)
  pila2.exchange()
  print("Pila Intercambiada: ", pila2)
  print("*"*50)

if __name__ == '__main__':
  main()
