# Indicar integrantes del grupo
# Aquino, Benjamin - Bravo, Agustin - Cafre, Marko

## Programar aquí los ejercicios desde 1 hasta 4 inclusive.

def factorial(numero):
  if numero < 0:
    return "ERROR: No es posible calcular el factorial de numeros negativos"
  res = 1
  for i in range(1, numero+1):
    res *= i
  return res

def suma_digitos(numero):
  res = 0
  while numero != 0:
    res += numero%10
    numero //= 10
  return res

def suma_lista(lista):
  res = 0
  for i in range(len(lista)):
    res += lista[i]
  return res

def es_multiplo(n, m):
  if n == 0 and m == 0:
    return True
  else:
    while n >= m:
      n -= m
    if n == 0:
      return True
    else:
      return False