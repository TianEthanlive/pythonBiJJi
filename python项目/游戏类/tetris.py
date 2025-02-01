import pygame # type: ignore
import random
import sys

# 定义游戏常量
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
FPS = 30
COLORS = [
    (0, 0, 0),      # 黑色 (背景)
    (255, 0, 0),    # 红色
    (0, 255, 0),    # 绿色
    (0, 0, 255),    # 蓝色
    (255, 255, 0),  # 黄色
    (255, 0, 255),  # 紫色
    (0, 255, 255),  # 青色
    (255, 255, 255) # 白色
]

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],          # I 形
    [[1, 1, 0], [0, 1, 1]],  # Z 形
    [[0, 1, 1], [1, 1, 0]],  # S 形
    [[1, 1], [1, 1]],        # O 形
    [[1, 1, 1], [0, 1, 0]],  # T 形
    [[1, 0, 0], [1, 1, 1]],  # L 形
    [[0, 0, 1], [1, 1, 1]]   # J 形
]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.randint(1, len(COLORS) - 1)

    def rotate(self):
        rows = len(self.shape)
        cols = len(self.shape[0])
        rotated = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 - i] = self.shape[i][j]
        self.shape = rotated

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_cells(self):
        cells = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    cells.append((self.x + x, self.y + y))
        return cells

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("俄罗斯方块")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.drop_speed = 500 # ms

        # time related
        self.last_drop_time = pygame.time.get_ticks()

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(GRID_WIDTH // 2 - len(shape[0]) // 2, 0, shape)

    def is_valid_move(self, piece):
        for x, y in piece.get_cells():
            if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or y < 0 or self.grid[y][x] != 0:
                return False
        return True

    def freeze_piece(self):
        for x, y in self.current_piece.get_cells():
            self.grid[y][x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.new_piece()

        if not self.is_valid_move(self.current_piece):
            self.game_over = True


    def clear_lines(self):
        lines_to_clear = []
        for y, row in enumerate(self.grid):
            if all(row):
                lines_to_clear.append(y)
        
        if lines_to_clear:
            for y in lines_to_clear:
                del self.grid[y]
                self.grid.insert(0, [0]* GRID_WIDTH)
            self.score += len(lines_to_clear) * 100

    def draw_grid(self):
         for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[cell], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, COLORS[7], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1) # draw boundary

    def draw_piece(self):
         for x, y in self.current_piece.get_cells():
             pygame.draw.rect(self.screen, COLORS[self.current_piece.color], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
             pygame.draw.rect(self.screen, COLORS[7], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(game_over_text, text_rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_piece.move(-1, 0)
                    if not self.is_valid_move(self.current_piece):
                        self.current_piece.move(1, 0)
                if event.key == pygame.K_RIGHT:
                     self.current_piece.move(1, 0)
                     if not self.is_valid_move(self.current_piece):
                        self.current_piece.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.current_piece.move(0, 1)
                    if not self.is_valid_move(self.current_piece):
                        self.current_piece.move(0, -1)
                        self.freeze_piece()
                if event.key == pygame.K_UP:
                    original_shape = self.current_piece.shape
                    self.current_piece.rotate()
                    if not self.is_valid_move(self.current_piece):
                        self.current_piece.shape = original_shape # rollback if invalid move
        
    def run(self):
        while True:
            self.screen.fill(COLORS[0])
            self.handle_input()
           
            if not self.game_over:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_drop_time > self.drop_speed:
                    self.current_piece.move(0, 1)
                    if not self.is_valid_move(self.current_piece):
                        self.current_piece.move(0, -1)
                        self.freeze_piece()
                    self.last_drop_time = current_time


                self.draw_grid()
                self.draw_piece()
                self.draw_score()
            else:
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Tetris()
    game.run()