from pygame import *
from random import randint
image_ping_pong = transform.scale(image.load('i.webp'),(700,500))
window = display.set_mode((700,500))
window.blit(image_ping_pong,(0,0))
display.set_caption('ping-pong')

class GameSprite (sprite.Sprite):
    def __init__(self,image_name,x,y,speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
    
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if self.rect.y < 450 :
            if keys_pressed[K_DOWN]:
                self.rect.y+= self.speed
        if self.rect.x >= 0 :
            if keys_pressed[K_UP]:
                self.rect.y -= self.speed
    
    def update1(self):
        keys_pressed = key.get_pressed()
        if self.rect.y < 450 :
            if keys_pressed[K_s]:
                self.rect.y+= self.speed
        if self.rect.x >= 0 :
            if keys_pressed[K_w]:
                self.rect.y -= self.speed

class Player2(GameSprite):    
    def __init__(self,image_name,x,y,speed,w,h):
        super().__init__(image_name,x,y,speed,w,h)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    def update(self):
        if self.rect.y >= 500 or self.rect.y <= 0:
            self.speed_y = -1*self.speed_y
        self.rect.x  += self.speed_x
        self.rect.y  += self.speed_y
    
sosiska1_right = Player('sosiska1.webp',50,250,10,100,80)
sosiska2_left = Player('sosiska2.jpg',550,250,10,100,80)
bulochka = Player2('bulochka.webp',300,250,5,130,80)

ochki1 = 0#левая сосиска
ochki2 = 0#правая сосиска
font.init()

f1 = font.Font(None, 36)
text1 = f1.render(str(ochki1), True,(180, 0, 0))
f2 = font.Font(None, 36)
text2 = f1.render(str(ochki2), True,(180, 0, 0))
f3 = font.Font(None, 40)
text3 = f3.render(('АЙ ТИГР'), True,(0, 180, 0))
f4 = font.Font(None, 40)
text4 = f4.render(('НЕ ТИГР'), True,(180, 0, 0))
window.blit(text4,(270,230))

clock = time.Clock()
sosiska1_right.update = sosiska1_right.update1
game = True
group = sprite.Group(sosiska1_right)
group.add(sosiska2_left)

finish = False

chetchik = 0

while game:
    window.blit(image_ping_pong,(0,0))
    
    if finish == True:
        chetchik += 1
        if chetchik >= 30 :
            finish = False
            chetchik = 0
            ochki1 = 0
            ochki2 = 0

        if ochki1 >= 10:
            text3 = f3.render(('АЙ ТИГР(1й победил)'), True,(0, 180, 0))
            window.blit(text3,(270,230))
    
              
        elif ochki2 >= 10:
            text4 = f4.render(('НЕ ТИГР(2й победил)'), True,(0, 0, 180))
            window.blit(text4,(270,230))
            if chetchik == 5:
                finish = False
    else:    
        if bulochka.rect.x >= 700:
            ochki1 += 1
            bulochka.rect.x = 320
            bulochka.rect.y = 220
            text1 = f1.render(str(ochki1), True,(180, 0, 0))
        if ochki1 >=10 :   
            finish = True
        if bulochka.rect.x <= 0:
            ochki2 += 1
            bulochka.rect.x = 320
            bulochka.rect.y = 220
            text2 = f2.render(str(ochki2), True,(180, 0, 0))
        if ochki2 >=10 :   
            finish = True
        if sprite.spritecollide(bulochka,group,False) :
            bulochka.speed_x = -1*bulochka.speed_x 
        
        
        window.blit(text1,(20,20))
        window.blit(text2,(600,20))
        bulochka.reset()
        group.draw(window)
        group.update()
        bulochka.update() 
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(60)
    display.update()
