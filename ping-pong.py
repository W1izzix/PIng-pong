from pygame import *
FPS = 60
clock = time.Clock()
game = True
finish = False
window = display.set_mode((700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y < 370:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y < 370:
            self.rect.y += self.speed
maga = Player('raketka.png',5,250,10,80,150)
maga2 = Player2('raketka.png',620,250,10,80,150)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((200,200,200))
        maga.reset()
        maga.update()
        maga2.reset()
        maga2.update()
    clock.tick(FPS)
    display.update()