#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

class CalzadoTipo:
    def __init__(self, descripcion: str) -> None:
        self.descripcion = descripcion

    def __eq__(self, other) -> bool:
      if not isinstance(other, CalzadoTipo):
        return False
      return self.descripcion == other.descripcion

    def __repr__(self) -> str:
      return self.descripcion

    def __str__(self) -> str:
      return repr(self)