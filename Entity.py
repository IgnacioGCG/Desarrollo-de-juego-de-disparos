class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def get_position(self, x, y):  
        self.x = x
        self.y = y

    def get_image(self):
        return self.image
    
    def set_image(self, image):
        self.image = image
        
    def collide(self, other):
        # Check for collision with another entity
        return (self.x < other.x + other.image.get_width() and
                self.x + self.image.get_width() > other.x and
                self.y < other.y + other.image.get_height() and
                self.y + self.image.get_height() > other.y)