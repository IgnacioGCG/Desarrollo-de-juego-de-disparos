from Oponent import Opponent

class Boss(Opponent):
    def __init__(self, name, health, damage, special_attack):
        super().__init__(name, health, damage)
        self.special_attack = special_attack

    def take_damage(self, amount):
        # Boss takes reduced damage
        reduced_damage = amount * 0.5
        self.health -= reduced_damage
        if self.health <= 0:
            self.health = 0
            self.defeated()
        print(f"{self.name} took {reduced_damage} damage! Remaining health: {self.health}")

    def attack(self):
        # Boss has a stronger attack
        print(f"{self.name} attacks with {self.damage} damage!")

    def use_special_attack(self):
        # Boss uses a special attack
        print(f"{self.name} uses a special attack: {self.special_attack}!")

    def defeated(self):
        print(f"{self.name} has been defeated! You win!")