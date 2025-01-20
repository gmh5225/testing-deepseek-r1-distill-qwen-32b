import pygame
import random
import time

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 添加方向常量
RIGHT = "RIGHT"
LEFT = "LEFT"
UP = "UP"
DOWN = "DOWN"

# 蛇的大小和速度
snake_block = 10
snake_speed = 30

# 初始化字体
font = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [width/6, height/3])

# 游戏主循环
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    direction = RIGHT
    change_to = direction

    while not game_over:
        while game_close == True:
            window.fill(BLACK)
            message("你输了！按 Q 退出或 C 重新开始", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    change_to = LEFT
                if event.key == pygame.K_RIGHT and direction != LEFT:
                    change_to = RIGHT
                if event.key == pygame.K_UP and direction != DOWN:
                    change_to = UP
                if event.key == pygame.K_DOWN and direction != UP:
                    change_to = DOWN

        direction = change_to

        if direction == LEFT:
            x1 -= snake_block
        elif direction == RIGHT:
            x1 += snake_block
        elif direction == UP:
            y1 -= snake_block
        elif direction == DOWN:
            y1 += snake_block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        window.fill(BLACK)
        
        # 绘制食物
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])

        # 更新蛇的位置和长度
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        
        # 绘制得分
        score = font.render(f"得分: {Length_of_snake - 1}", True, WHITE)
        window.blit(score, [0, 0])
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        time.sleep(1 / snake_speed)

    pygame.quit()
    quit()

# 开始游戏
gameLoop()

