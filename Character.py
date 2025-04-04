from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = True

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        # Implement movement logic here
        pass

    def shoot(self):
        """
        Handles the shooting action of the character.
        """
        # Implement shooting logic here
        pass

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        # Implement collision logic here
        if self.lives > 0:
            self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False
            # Handle character death (e.g., respawn, game over, etc.)
    def respawn(self, x, y):
        """
        Respawns the character at the specified coordinates.
        :param x: The x-coordinate for respawn.
        :param y: The y-coordinate for respawn.
        """
        self.x = x
        self.y = y
        self.lives = 3
        self.is_alive = True  # Reset lives and status on respawn
    def get_lives(self):
        """
        Returns the number of lives remaining.
        :return: The number of lives.
        """
        return self.lives