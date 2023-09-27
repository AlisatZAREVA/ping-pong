from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_sped, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y)) 
        self.speed = pl_sped 
        self.rect = self.image.get_rect()
        self.rect.x = pl_x 
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 600
win_height = 500
FPS = 60
clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('ping-pong')
background = transform.scale(image.load('palm.jpg'),(win_width, win_height))
run = True
ball =GameSprite('ball.png',200,200,10,60,60)
player1 = Player('line.png', 0,200,10,30,100)
player2 = Player('line.png', 570,200,10,30,100)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(background, (0, 0))
    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    ball.reset()
    display.update()
    time.delay(50)
