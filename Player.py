from Character import Character

class Player(Character):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3

    def move(self, direction):
        # Logic for player movement
        pass

    def shoot(self):
        # Logic for shooting
        pass    
    def reset(self):
        """
        Resets the player's score and lives.
        """
        self.score = 0
        self.lives = 3
        self.is_alive = True
    def collide(self, other_entity):
        return super().collide(other_entity.name)