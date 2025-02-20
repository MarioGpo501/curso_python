""" 
    clase Team: Equipo 

"""

from Athlete import Athlete
from Sport import Sport
class Team:
    """ Clase para representar un equipo """
    def __init__(self,name:str, sport:Sport, players:list):
        """ Constructor de la clase Team """
        self.name = name
        self.sport = sport
        self.players = players

    def __str__(self):
        """ Método para representar la calse como String """
        return f"Team: {self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        """ Método para representar la clase como String """
        return f"Team(name='{self.name}', sport={self.sport}, players={self.players})"
    
    def to_json(self)->dict:
        """ Método para representar la clase como diccionario """
        return {"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}
    

if __name__ == "__main__":
    a1 = Athlete("Michael J.")
    a2 = Athlete("Lebron J.")
    a3 = Athlete("Stephen C.")
    a4 = Athlete("Shaquil O.")
    a5 = Athlete("Kobe B.")

    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))
    print(lakers.to_json())