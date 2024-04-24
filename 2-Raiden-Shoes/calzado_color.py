#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

from typing import Optional

class CalzadoColor:
    def __init__(self, primario: str, secundario: str = "") -> None:
        self.primario = primario
        self.secundario = secundario

    def __eq__(self, other) -> bool:
      if not isinstance(other, CalzadoColor):
        return False
      return self.primario == other.primario \
             and self.secundario == other.secundario

    def __repr__(self) -> str:
      return f"(Color Primario: {self.primario}, Color Secundario: {self.secundario})"

    def __str__(self) -> str:
      return repr(self)