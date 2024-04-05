import pygame
from pygame import *
from random import randint

font.init()
font_text = font.Font(None, 36)

WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 3000

def gencolor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

background = gencolor()
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
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < WIDTH - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < WIDTH - 80:
            self.rect.y += self.speed

Engine = True

while Engine:
    window.fill(background)
    for e in event.get():
        if e.type == QUIT:
            Engine = False  
    display.update()
    clock.tick(FPS)