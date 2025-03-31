from Entity import Entity

class Shot(Entity):
    def move(self):
        # Logic to move the shot
        pass

    def hit_target(self, target):
        # Logic to check if the shot hits the target
        pass
    def reset(self):
        """
        Resets the shot's state.
        """
        # Logic to reset the shot's position or state
        pass
    def get_position(self):
        """
        Returns the current position of the shot.
        :return: A tuple (x, y) representing the shot's position.
        """
        return self.x, self.y
    def set_position(self, x, y):
        """
        Sets the position of the shot.
        :param x: The x-coordinate to set.
        :param y: The y-coordinate to set.
        """
        self.x = x
        self.y = y
    def get_image(self):
        """
        Returns the image of the shot.
        :return: The image of the shot.
        """
        return self.image
    def set_image(self, image):
        """
        Sets the image of the shot.
        :param image: The image to set.
        """
        self.image = image
    def collide(self, other_entity):
        """
        Checks for collision with another entity.
        :param other_entity: The entity to check collision with.
        :return: True if there is a collision, False otherwise.
        """
        return super().collide(other_entity)
    def draw(self, screen):
        """
        Draws the shot on the screen.
        :param screen: The screen to draw on.
        """
        screen.blit(self.image, (self.x, self.y))
    def get_speed(self):
        """
        Returns the speed of the shot.
        :return: The speed of the shot.
        """
        return self.speed