#Integrantes: Aquino Benjamin - Bravo Agustin - Cafre Marko


class Bando:
  GOOD = "Good"
  BAD = "Bad"
  NEUTRAL = "Neutral"
  REFORMED = "Reformed Criminals"
  EMPTY = ""

  def __init__(self, bando: str) -> None:
    self.bando = bando

  def __eq__(self, other) -> bool:
    if not isinstance(other, Bando):
      return False
    return other.bando == self.bando

  def __str__(self) -> str:
    return f"Bando: {self.bando}"
