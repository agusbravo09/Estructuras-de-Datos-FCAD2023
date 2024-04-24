# Indicar integrantes del grupo
# Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

# Demostrar el correcto funcionamiento de las funciones aquí.
if __name__ == '__main__':
  import funciones

  num = int(input("Ingrese un numero: "))
  print("El factorial es:", funciones.factorial(num))

  print('*' * 50)

  num = abs(int(input("Ingrese un numero: ")))
  print("La suma de los digitos es:", funciones.suma_digitos(num))

  print('*' * 50)

  lista = [1, 2, 3, 4, 5, 6]
  print("La suma de los elementos de la lista es: ",
        funciones.suma_lista(lista))

  print('*' * 50)

  n = abs(int(input("Ingrese un numero n: ")))
  m = abs(int(input("Ingrese un numero m: ")))
  print("Es multiplo:", funciones.es_multiplo(n, m))
