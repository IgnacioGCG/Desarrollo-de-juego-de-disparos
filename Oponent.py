from Character import Character

class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def move(self):
        # Implementar lógica de movimiento del oponente
        pass

    def shoot(self):
        # Implementar lógica de disparo del oponente
        pass    
    def collide(self, other_entity):
        # Implementar lógica de colisión del oponente
        pass
    def get_is_star(self):  
        """
        Returns whether the opponent is a star.
        :return: True if the opponent is a star, False otherwise.
        """
        return self.is_star
    def set_is_star(self, is_star):
        """
        Sets whether the opponent is a star.
        :param is_star: True if the opponent is a star, False otherwise.
        """
        self.is_star = is_star
    def reset(self):
        """""
        Resets the opponent's state.
        """
        self.is_star = False