# projectile.py
import pygame
from config import GRID_SIZE

class Projectile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, speed, damage):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GRID_SIZE // 2, GRID_SIZE // 2))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.damage = damage

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 800:
            self.kill()  # 超出屏幕删除