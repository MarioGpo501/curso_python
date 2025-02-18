""" clase atleta """

class Athlete:
    def __init__(self, name:str):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Athlete('{self.name}')"
    
    def display(self):
        print(f"{self.name}")

if __name__ == "__main__":
    atleta = Athlete("Lionel Messi")
    atleta.display() 
    print(atleta)
    print(repr(atleta))
    print(f"Atleta:{id(atleta)}")
    b = eval(repr(atleta))
    print(b)
    print(f"b:{id(b)}")