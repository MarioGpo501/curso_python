""" Clase Game: Juego entre dos equipos """

from Athlete import Athlete
from Sport import Sport
from Team import Team   
from random import choice
import json


class Game: 
    sports_dict = {
            'LMP': [x for x in range(0,11)],
            'NBA': [x for x in range(50,136)],
            'NFL': [x for x in range(0,61)],
            'MLB': [x for x in range(0,21)],
            'MLX': [x for x in range(0,11)],
            'FIFA': [x for x in range(0,11)],
        }

    """ clase game: Juego entre dos equipos """
    def __init__(self, A:Team, B:Team):
        """ Contructor de la clase Game """ 
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0  

    def play(self):
        """ Método para simular un juego """
        league = self.A.sport.league
        points = self.sports_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self):
        """ Metodo para representar la clase como string """
        return f"Game: {self.A.name}: {self.score[self.A.name]} - {self.B.name}: {self.score[self.B.name]}"
    
    def to_json(self):
        """ Método para representar la clase como diccionario """
        return {"A":self.A.to_json(), "B":self.B.to_json(), "score":self.score}

if __name__ == "__main__": 
    dt = ['Jordan', 'Kobe', 'Lebron', 'Shaq', 'Curry']
    cz = ['Bjovik', 'Kareem', 'Magic', 'Worthy', 'Kobe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("Basketball", 5, "NBA")
    team_a = Team("Dream team", basketball, players_a)
    team_b = Team("Czeck Rep", basketball, players_b)
    game = Game(team_a, team_b) 
    print(game)
    game.play()
    print(game)
    print("-----------------")
    print(repr(game))
    print(game.to_json())
    filename_json = "game.json"
    with open(filename_json, "w", encoding="utf8") as f:
        json.dump(game.to_json(), f, ensure_ascii=False, indent=4)
    print(f"Archivo {filename_json} creado con éxito")
    print("-----------------")
    
        

        
