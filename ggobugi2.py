import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("꼬부기는 리자몽이 싫어")
clock = pygame.time.Clock()
background = pygame.image.load("C:/HAK\HakPython/mini_project/image/forest.jpg")
character = pygame.image.load("C:/HAK/HakPython/mini_project/image/ggobug.png")
enemy = pygame.image.load("C:/HAK/HakPython/mini_project/image/lizamong.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
enemy_x_pos = random.randint(0, (screen_width - character_width))
enemy_y_pos = 0
to_x = 0
to_y = 0

character_speed = 0.4
enemy_speed = 1.1
game_over_font = pygame.font.SysFont("Arial",80,True,False)
game_font = pygame.font.SysFont("Arial",95,True,False)
press_font = pygame.font.SysFont("Arial",40,True,True)
score_font = pygame.font.SysFont("Hello World",70,False,False)
timer_font = pygame.font.SysFont("Hello World",50,False,False)
avoided_font = pygame.font.SysFont("Hello World",50,False,False)
start_ticks = pygame.time.get_ticks()
avoid_enemies = 0

def game_start():
    screen.blit(background, (0, 0))
    text_Title1= game_font.render("Ggobugi hates Lizamong", True, "hotpink")
    screen.blit(text_Title1, (screen_width - 970, screen_height - 550))
    text_Title2= press_font.render("To start, Press Space key", True, "white")
    screen.blit(text_Title2, (screen_width - 700, screen_height - 250))
    pygame.display.update()
    wait_for_key()

def wait_for_key():
    global avoid_enemies
    global elapsed_time
    global start_ticks
    global enemy_speed
    #global chracter_x_pos
    #global chracter_y_pos
    avoid_enemies=0
    elapsed_time = (pygame.time.get_ticks())
    global running
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_ticks = pygame.time.get_ticks()
                    enemy_speed = 1.1
                    #chracter_x_pos = (screen_width / 2) - (character_width / 2) #플레이어 화면 정가운데 위치
                    #chracter_y_pos = (screen_height / 2) - (character_height / 2)
                    running = True ##게임 실행 동작
                    waiting = False
                    
def game_over_():    
    if not running:
        return
    
    # level_control = 0
    # total_level = 0
    # player_to_x = 0
    # player_to_y = 0
    
    # avoided.clear() #리스트 초기화
    
    screen.blit(background, (0, 0))#게임오버 됐을 때 화면 꾸미기
    text_gameover1= game_over_font.render("Game   Over", True, "red")
    screen.blit(text_gameover1, (screen_width - 700, screen_height - 600))
    text_gameover2= press_font.render("Press a Space key to play again", True, "white")
    screen.blit(text_gameover2, (screen_width - 750, screen_height - 250))
    text_gameover_score= score_font.render("Score : {}".format(avoid_enemies), True, "orange")
    
    screen.blit(text_gameover_score, (screen_width - 600, screen_height - 500))
    #avoid_enemies = 0 #점수는 화면에 표시해주고 마지막에 초기화
    pygame.display.flip()
    wait_for_key()


running = False
game_start()
while running:
    
    dt = clock.tick(30)
    to_y = 0
    to_y += enemy_speed       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    enemy_y_pos += to_y * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, (screen_width - character_width))
        enemy_y_pos = 0
        avoid_enemies += 1
        if avoid_enemies > 4:
            enemy_speed = 1.4
        elif avoid_enemies > 8:
            enemy_speed = 1.8
        elif avoid_enemies > 12:
            enemy_speed = 3

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = timer_font.render('Time:{}'.format(round(elapsed_time, 2)), True, (255, 255, 255))
    avoided = avoided_font.render('dodge: {}'.format(avoid_enemies), True, (255, 255, 255))
    game_over = game_over_font.render('Oops!', True, (255, 255, 255))
   
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(avoided, (200, 10))

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        screen.blit(game_over, (50, 100))
        game_over_()

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()