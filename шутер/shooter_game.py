#Создай собственный Шутер!

from pygame import *
from random import *
w = 700
h = 500
windows = display.set_mode((w,h))
display.set_caption("labirint")
bg = image.load("galaxy.jpg")
bg = transform.scale(bg, (700,500))
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
class GameSprite(sprite.Sprite):
    def __init__(self, x,y,filename):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.face = "right"
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= 10
        if keys[K_d]:
            self.rect.x += 10
        if self.rect.x > 700:
            self.rect.x = -100
        if self.rect.x < -100:
            self.rect.x = 700
        self.reset()
    def shoot(self):
        b = Bullet(x=self.rect.x + 15 , y=self.rect.y , filename="bullet.png")
        PULE.add(b)
        keys = key.get_pressed()
        if keys[K_LCTRL]:
            d = Super_bullet(x=self.rect.x + 15 , y=self.rect.y , filename="bullet.png")
            PULE.add(d)


class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if not keys[K_KP6]:
            self.rect.y += randint(-1,10)
            self.rect.x += randint(-1,1)
        if self.rect.y > 500 or sprite.collide_rect(self, player):
            self.rect.y = -150
            human_health_rect.width -= 50
            if human_health_rect.width <= 0:
                exit()
         

        self.reset()

class Meteorit(Enemy):
    def __init__(self, x,y,filename="byliwnic.png"):
        super().__init__(x,y,filename)
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(45,55))
        self.image = transform.rotate(self.image,35)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 15
        if self.rect.y < 0:
            PULE.remove(self)
        self.reset()
    def __init__(self, x,y,filename):
        super().__init__(x,y,filename)
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.reset()

class Super_bullet(Bullet):
    def update(self):
        self.rect.y -= 15
        self.rect.x -= 3
        if self.rect.y < 0:
            PULE.remove(self)
        self.reset()

human_health_rect = Rect(0,450,w,15)

UFOS = sprite.Group()
PULE = sprite.Group()

player = Hero(x=500,y=400,filename="rocket.png")
warrior = Enemy(x=400,y=-150,filename="ufo.png")
warrior1 = Enemy(x=300,y=-150,filename="ufo.png")
warrior2 = Enemy(x=200,y=-150,filename="ufo.png")
warrior3 = Enemy(x=40,y=-150,filename="ufo.png")
warrior4 = Enemy(x=350,y=-150,filename="ufo.png")
kamen = Meteorit(x=87,y=-150)

UFOS.add(warrior,warrior1,warrior2,warrior3,warrior4,kamen)


clock = time.Clock()
FPS = 60
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYUP:
            if i.key == K_SPACE:
                player.shoot()

    clock.tick(FPS)
    windows.blit(bg, (0,0))
    draw.rect(windows,(255,255,255),human_health_rect)
    UFOS.update()
    player.update()
    PULE.update()
    meet = sprite.groupcollide(UFOS, PULE, False, False)
    for i in meet:
        i.rect.y = 0
        i.rect.x = randint(0,600)
    display.update()



