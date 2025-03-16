# main.py
import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GRID_SIZE, PLANT_SPACE_X, PLANT_SPACE_Y
from plant import Sunflower, Peashooter
from zombie import BasicZombie
from projectile import Projectile


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Plants vs Zombies (Simple)")
    clock = pygame.time.Clock()

    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


    plants = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    
    
    sun_amount = 100 # 初始阳光数
    font = pygame.font.Font(None, 36) # 创建一个font对象

    def draw_sun_count():
      text_surface = font.render(f"Sun:{sun_amount}",True,(255,255,0))
      screen.blit(text_surface,(10,10))

    # 游戏主循环
    running = True
    zombie_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x = (x - PLANT_SPACE_X) // GRID_SIZE
                grid_y = (y - PLANT_SPACE_Y) // GRID_SIZE

                if  0 <= grid_x <= 8 and 0 <= grid_y <= 4:
                    plant_x = PLANT_SPACE_X + grid_x * GRID_SIZE
                    plant_y = PLANT_SPACE_Y + grid_y * GRID_SIZE
                    
                    # 点击一个格子，判断当前要种什么植物
                    
                    
                    if sun_amount >= 50:
                      new_sunflower = Sunflower(plant_x, plant_y)
                      plants.add(new_sunflower)
                      sun_amount -= 50
                    elif sun_amount >= 100:
                      new_peashooter = Peashooter(plant_x, plant_y)
                      plants.add(new_peashooter)
                      sun_amount -= 100

        # 生成僵尸逻辑
        zombie_timer +=1
        if zombie_timer % 120 == 0: # 每两秒生成一个僵尸
            random_y = random.randint(0,4)
            zombie_y = PLANT_SPACE_Y + random_y * GRID_SIZE
            new_zombie = BasicZombie(zombie_y)
            zombies.add(new_zombie)

        # 更新植物、僵尸、投射物
        for plant in plants:
             if isinstance(plant,Sunflower):
              sun_produced = plant.update()
              sun_amount += sun_produced

             if isinstance(plant,Peashooter):
                can_shoot = plant.update()
                if can_shoot:
                  new_projectile = Projectile("images/pea.png", plant.rect.right, plant.rect.centery, 10, plant.attack_damage)
                  projectiles.add(new_projectile)
            
        zombies.update()
        projectiles.update()
        

        # 碰撞检测(豌豆打僵尸)
        projectile_hit_zombies = pygame.sprite.groupcollide(projectiles, zombies, True, False)
        for projectile,zombies_hit in projectile_hit_zombies.items():
             for zombie in zombies_hit:
                zombie.take_damage(projectile.damage)

        # 碰撞检测(僵尸吃植物)
        zombie_hit_plants = pygame.sprite.groupcollide(zombies, plants, False, False)
        for zombie,plants_hit in zombie_hit_plants.items():
            for plant in plants_hit:
                 plant.take_damage(1) # 持续伤害

        # 绘制游戏元素
        screen.blit(background, (0, 0))
        plants.draw(screen)
        zombies.draw(screen)
        projectiles.draw(screen)
        draw_sun_count()


        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()