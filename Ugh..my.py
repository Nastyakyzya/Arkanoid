import pygame
import time
from random import randint
pygame.init()

ulta=(41, 132, 240)
okno=pygame.display.set_mode((500, 500))
okno.fill(ulta)

cl= pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = ulta
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(okno,self.fill_color,self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

#клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image=pygame.image.load(filename)
    def draw(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

platform_x=200
platform_y=260

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', platform_x, platform_y, 100, 30)
#cтворення ворогів
monster_x=5
monster_y=5
count=9
monsters=[]
for j in range(3):
    y = monster_y+(55*j)
    x = monster_x+(28*j)
    for i in range(count):
        monster=Picture('enemy.png', x, y, 50, 50)
        monsters.append(monster)
        x=x+55
    count=count-1


game_over=False

ball_speed_x=3
ball_speed_y=3

while not game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform.rect.x>0:
        platform.rect.x-=5
    if keys[pygame.K_RIGHT] and platform.rect.x<400:
        platform.rect.x+=5
    #рух м'яча, поки триває гра
    ball.rect.x+=ball_speed_x
    ball.rect.y+=ball_speed_y
    #зіткнення м'яча зі стінами
    if ball.rect.x <=0 or ball.rect.x >=450:
        ball_speed_x= -ball_speed_x
    if ball.rect.y  <=0:
        ball_speed_y = -ball_speed_y
    #зіткнення з платформою
    if ball.rect.colliderect(platform.rect):
        ball_speed_y = - ball_speed_x

    okno.fill(back)
    for m in monsters:
        m.draw()
    #видалення монстра зі списку і життя в цілому
    for m in monsters:
        if ball.rect.colliderect(ball.rect):
            monster.remove(m)
            ball_speed_y *= -1
            
    ball.draw()
    platform.draw()
    #м'яч торкається платформи
    if ball.rect.colliderect(platform.rect):
        ball_speed_y*=-1

    if not monsters:
        font2=pygame.font.Font(None, 40)
        win=font1.render('You win) Dummy...',  True,(255, 0 ,0 ))
        okno.blit(win, (200, 250)
        pygame.display.update()
        game_over = True

    platform.draw()
    ball.draw()

    if ball.rect.y>220:
        font1=pygame.font.Font(None, 40)
        lose=font1.render('You looooose) Dummy...',  True,(255, 0 ,0 ))
        okno.blit(lose, (200, 250))
        pygame.display.update()
        game_over = True


    pygame.display.update()
    cl.tick(40)







