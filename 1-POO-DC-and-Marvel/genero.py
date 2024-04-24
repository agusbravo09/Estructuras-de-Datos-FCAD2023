#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko


class Genero:
  FEMALE = "Female"
  MALE = "Male"

  def __init__(self, genero) -> None:
    self.genero = genero

  def __eq___(self, other) -> bool:
    if not isinstance(other, Genero):
      return False
    return self.genero == other.genero

  def __str__(self) -> str:
    return f"Genero: {self.genero}"
