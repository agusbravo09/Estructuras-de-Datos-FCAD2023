#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor
from calzado_talle import CalzadoTalle

class Calzado:
    def __init__(self, sku: int, nombre: str, descripcion: str, tipo: CalzadoTipo, talle: CalzadoTalle, color: CalzadoColor, cantidad: int, precio: float) -> None:
        self._sku = sku
        self.nombre = nombre
        self.descripcion = descripcion 
        self.tipo = tipo
        self.talle = talle
        self.color = color
        self._cantidad = cantidad  # Cantidad de Existencias de este producto
        self._precio = precio
  
    @property
    def cantidad(self) -> int:
      return self._cantidad
      
    @property
    def precio(self) -> float:
      return self._precio
      
    @property
    def sku(self) -> int:
      return self._sku

    @property
    def total(self) -> float:
      return self._cantidad * self._precio
      
  
    @cantidad.setter
    def cantidad(self, cantidad: int) -> None:
      if cantidad < 0:
        raise ValueError("No se puede modificar el atributo Cantidad")
      else:
        self._cantidad = cantidad

    @precio.setter
    def precio(self, precio: float) -> None:
      if precio < 0:
        raise ValueError("No se puede modificar el atributo Precio")
      else:
        self._precio = precio

    @sku.setter
    def sku(self, sku: int) -> None:
      if sku >= 1:
        self._sku = sku
      else:
        raise ValueError("No se puedde modificar el atributo SKU")
      
    def __eq__(self, other) -> bool:
      if not isinstance(other, Calzado):
        return False
      return self._sku == other._sku \
             and self.nombre == other.nombre \
             and self.descripcion == other.descripcion \
             and self.tipo == other.tipo \
             and self.talle == other.talle \
             and self.color == other.color \

    def __repr__(self) -> str:
      return f"SKU: {self._sku}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nTipo: {self.tipo}\nTalle: {self.talle}\nColor: {self.color}\nCantidad: {self._cantidad}\nPrecio: {self._precio}\n"

    def __str__(self) -> str:
      return repr(self)