from pygame import *
from time import time as timer
FPS = 60
clock = time.Clock()
game = True
finish = False
speed_x = 5
speed_y = 5
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
font.init()
font1 = font.SysFont('Arial',36)
levo = font1.render('Player1 win',10,(255,0,0))
pravo = font1.render('Player2 win',10,(0,255,0))
maga = Player('raketka.png',5,250,10,80,150)
maga2 = Player2('raketka.png',620,250,10,80,150)
ball = GameSprite('myach.png',340,150,10,50,50)
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
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(maga,ball) or sprite.collide_rect(maga2,ball):
        speed_x *= -1
    if ball.rect.y < 0 or ball.rect.y > 470:
        speed_y *= -1
    # if ball.rect.x > 700 or ball.rect.x < 0:
    #     speed_x *= -1 
    if ball.rect.x < -10:
        window.blit(pravo,(200,200))
        # ball.kill()
        # maga.kill()
        # maga2.kill()
        # window.blit(pravo,(200,200))
        # time.delay(5000)
        # maga.reset()
        # maga.update()
        # maga2.reset()
        # maga2.update()
        # ball.reset()
    if ball.rect.x > 710:
        window.blit(levo,(200,200))
        # ball.kill()
        # maga.kill()
        # maga2.kill()
        # window.blit(levo,(200,200))
        # time.delay(5000)
        # maga.reset()
        # maga.update()
        # maga2.reset()
        # maga2.update()
        # ball.reset()
    clock.tick(FPS)
    display.update()