import pygame
from pygame import *
from random import randint
 
font.init()
font_text = font.Font(None, 36)
font_score = font.Font(None, 50)

lose1 = font_text.render("PLAYER 1 LOSE", True, (100, 0, 0))
lose2 = font_text.render("PLAYER 2 LOSE", True, (100, 0, 0))
 
WIDTH = 600
HEIGHT = 500
FPS = 60
score1 = 0
score2 = 0
speed_x = 3
speed_y = 3
WIN_SCORE = 10

background = (randint(0, 255), randint(0, 255), randint(0, 255))
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Pingpong2DEngine")
clock = time.Clock()
 
class GameSprite(sprite.Sprite):
    def __init__(self, p_image: str, x: int, y: int, h: int, w: int, speed: int):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))
 
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WIDTH - 200:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WIDTH - 200:
            self.rect.y += self.speed

racket1 = Player("racket.png", 30, 200, 100, 25, 4)
racket2 = Player("racket.png", 517, 200, 100, 25, 4)
ball = GameSprite("tenis_ball.png", 200, 200, 50, 50, 4)

Engine = True
finish = False
 
while Engine:
    for e in event.get():
        if e.type == QUIT:
            Engine = False
    if not finish:
        window.fill(background)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        offset = (ball.rect.y - racket1.rect.y) / (racket1.rect.height - ball.rect.height)
        speed_y = 2 * offset - 1
        speed_x *= -1
    if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        score2 += 1
        ball.rect.x = 200
        ball.rect.y = 200
        speed_x = 3  # мяч будет лететь вправо
    if ball.rect.x > WIDTH:
        score1 += 1
        ball.rect.x = 200
        ball.rect.y = 200
        speed_x = -3  # мяч будет лететь влево
    if score1 >= WIN_SCORE or score2 >= WIN_SCORE:
        finish = True
        if score1 > score2:
            window.blit(lose2, (200, 200))
        else:
            window.blit(lose1, (200, 200))
    score_text = f"{score1}:{score2}"
    score_img = font_score.render(score_text, True, (255, 255, 255))
    score_rect = score_img.get_rect(center=(WIDTH // 2, 50))
    window.blit(score_img, score_rect)
    if finish == True:
        Engine = False
    display.update()
    clock.tick(FPS)
