# zombie.py
import pygame
from config import GRID_SIZE, ZOMBIE_START_X

class Zombie(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 100  # 僵尸的生命值
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def take_damage(self, damage):
       self.health -= damage
       if self.health <=0:
         self.kill()


class BasicZombie(Zombie):
    def __init__(self, y):
        super().__init__("images/zombie.png", ZOMBIE_START_X, y, 1)