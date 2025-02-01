# plant.py
import pygame
from config import GRID_SIZE

class Plant(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 100  # 植物的生命值

    def update(self):
        pass # 基类 update 不做任何事
    
    def take_damage(self, damage):
      self.health -= damage
      if self.health <= 0:
        self.kill() #移除精灵

class Sunflower(Plant):
    def __init__(self, x, y):
        super().__init__("images/sunflower.png", x, y)
        self.sun_production_rate = 10  # 向日葵产阳光的速率
        self.sun_production_time = 0

    def update(self):
         self.sun_production_time += 1
         if self.sun_production_time % 60 == 0:
             return self.sun_production_rate
         return 0


class Peashooter(Plant):
    def __init__(self, x, y):
        super().__init__("images/peashooter.png", x, y)
        self.attack_damage = 20
        self.attack_speed = 30
        self.attack_timer = 0

    def update(self):
        self.attack_timer += 1
        if self.attack_timer >= self.attack_speed:
            self.attack_timer = 0
            return True  # 返回 True 代表可以发射豌豆
        return False