#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko

from personaje import Personaje
from bando import Bando
from genero import Genero

from comics_admin_abstract import ComicsAdminAbstract

class ComicsAdmin(ComicsAdminAbstract):
  
  def agregar_desde_csv(self, ruta: str) -> None:
    import csv
    with open(ruta) as archivo:
      pjs = csv.reader(archivo, delimiter=',')
      next(pjs)
      for i in pjs:
        self._lista.append(Personaje(i[0], i[1], i[3], i[6], i[10]))
        
  def __str__(self) -> str:
    text = ""
    for pj in self._lista:
      text += "Personaje:"+str(pj)+"\n"
    return text

  def filtrar_por_bando(self, bando: Bando, limite: int = 0):
    listaFiltradaBando = []
    lim = 0
    for i in self._lista:
      if i.bando == bando:
        listaFiltradaBando.append(i)
        lim += 1
      if lim == limite:
        break;
    return listaFiltradaBando

  def filtrar_por_genero(self, genero: Genero, limite: int = 0):
    listaFiltradaGenero = []
    lim = 0
    for i in self._lista:
      if i.genero == genero:
        listaFiltradaGenero.append(i)
        lim += 1
      if lim == limite:
        break
    return listaFiltradaGenero

  def contar_por_universo(self):
    dc = 0
    marvel = 0
    for i in self._lista:
      match i.universo:
        case "DC":
          dc += 1
        case "Marvel":
          marvel += 1
    tupla = (dc, marvel)
    return tupla