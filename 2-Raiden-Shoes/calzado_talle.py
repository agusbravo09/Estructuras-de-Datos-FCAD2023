#Integrantes: Aquino Benjamin, Bravo Agustin, Cafre Marko

class CalzadoTalle:
    def __init__(self, descripcion: str, medida_en_cm: float) -> None:
        self.descripcion = descripcion
        self.medida_en_cm = medida_en_cm

    def __eq__(self, other) -> bool:
      if not isinstance(other, CalzadoTalle):
        return False
      return self.decripcion == other.descripcion \
           and self.medida_en_cm == other.medida_en_cm

    def __repr__(self) -> str:
      return f"{self.descripcion}, Medida (en cm): {self.medida_en_cm}"

    def __str__(self) -> str:
      return repr(self)
