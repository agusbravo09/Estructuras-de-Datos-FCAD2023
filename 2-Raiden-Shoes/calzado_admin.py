#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

from calzado_admin_abstract import CalzadoAdminAbstract
from calzado import Calzado
from calzado_tipo import CalzadoTipo

class CalzadoAdmin(CalzadoAdminAbstract):
  def __repr__(self) -> str:
    text = ""
    for i in self._lista:
      text += "Calzado: "+str(i)+" \n"
    return text

  def __str__(self) -> str:
    return repr(self)

  def agregar(self, item: Calzado) -> None:
      for i in self._lista:
        if item.sku == i.sku:
          raise ValueError("SKU EN USO")
      self._lista.append(item)

  
  def filtrar_por_tipo(self, tipo: CalzadoTipo):
    listaCalzadosPorTipo = []
   # print(self._lista[0].tipo) <- Deportivas
   # print(tipo.descripcion)  <- Deportivas
   # print(str(self._lista[0].tipo) == str(tipo.descripcion)) <- true
    for i in self._lista:
      if i.tipo.__eq__(tipo):
        listaCalzadosPorTipo.append(i)
    return listaCalzadosPorTipo

  def filtrar_precio_entre(self, desde: float = 0.00, hasta: float = 0.00):
    if (desde == 0.00 and hasta == 0.00) or hasta < desde:
      raise ValueError("No se ha podido filtrar por precio")
    else:
      listaFiltroPrecio = []
      for i in self._lista:
        if i.precio >= desde and i.precio <= hasta:
          listaFiltroPrecio.append(i)
      return listaFiltroPrecio

  def cantidad_productos(self) -> int:
    total = 0
    for i in self._lista:
      total += i.cantidad
    return total

  def total_productos(self) -> float:
    total = 0.00
    for i in self._lista:
      total += i.total
    return total