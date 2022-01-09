class Dog:
    def __init__(self, character):
        self.character = character
        
    def move(self):
        print("moved")
    
class Poodle(Dog):
    def __init__(self, shed):
        self.shed = shed
    
    
dog1 = Poodle("none")
dog1.move()
