## Programar aquí el ejercicio 7
## Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko
def cantidad_por_bando():
  import csv
  with open('marvel_dc_characters.csv') as superheroes:
    characters = csv.reader(superheroes, delimiter=',')
    bandos = {}
    next(characters) #<-- saltea el encabezado
    
    for i in characters:
      if i[3] in bandos:
        bandos[i[3]] += 1
      else:
        bandos[i[3]] = 1
          
  return bandos  