#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko


class Universo:

  def __init__(self, universo: str) -> None:
    self.universo = universo

  def __eq__(self, other) -> bool:
    if not isinstance(other, Universo):
      return False
    return self.universo == other.universo

  def __str__(self) -> str:
    return f"Universo: {self.universo}"
