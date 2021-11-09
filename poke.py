
from pathlib import Path
# Create a pokemon
# Look at it
# Feed them (increase health)
# Make them battle and decide a winner

class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.max_hp = max_hp
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp

    def __str__(self):
        return f"{self.name}, {self.primary_type}"

    def feed(self):
        if self.hp < self.max_hp:  
            self.hp += 1
            print(f'{self.name} now has {self.hp} HP.')
        else:
            print(f'{self.name} has full HP')
    def battle(self, other):
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f'Battle: {self.name} vs. {other.name}')
        print(f'{self.name} fought {other.name} and {result}')

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lost", 1: "won", -1: "tied"}
        mapping = {'water': 0, "fire": 1, "grass": 2}
        winlosematrix = [
            [-1, 1, 0], #water
            [0, -1, 1], #fire
            [1, 0, -1],
        ]
        mapping["water"]
        winlose = winlosematrix[mapping[type1]][mapping[type2]]
        return result[winlose]

if __name__ == '__main__':
    firstcard = Pokemon("bulbasaur", "grass", 100)
    secondcard = Pokemon("charmander", "fire", 150)
    print(firstcard)
    print(secondcard)