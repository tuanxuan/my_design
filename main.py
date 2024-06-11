import pygame
import os
import random
from fatherbullets import Father_Bullets
from fatherspaceship import Father_Spaceship
from explosion import Explosion
from enemybullets import Enemy_Bullets
from enemyspaceship import Spaceship_enemys
from mybullets import Bullets
from myspaceship import My_spaceship

# Define constants
WIDTH = 600
HEIGHT = 800
FPS = 50
POWERUP_TIME = 5000

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Asset folders
img_dir = os.path.join(os.path.dirname(__file__), 'assets')
sound_folder = os.path.join(os.path.dirname(__file__), 'sounds')

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space War')
clock = pygame.time.Clock()

# Define game variables
rows = 5
cols = 5
enemy_cooldown = 1000
last_enemy_bullet = pygame.time.get_ticks()
game_over = 0
score = 0

# Load background
bg = pygame.image.load(os.path.join(img_dir, 'background.png')).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))  # Ensure the background is the same size as the screen
bg_height = bg.get_height()
scroll_speed = 5
bg_y1 = 0
bg_y2 = -bg_height + 5

# Font for drawing text
font_name = pygame.font.match_font('arial')

# Sprite groups
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
Spaceship_enemys_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

# Create player
my_spaceship = My_spaceship(int(WIDTH / 2), HEIGHT - 100, 3, img_dir, sound_folder)
my_spaceship_group = pygame.sprite.Group()
my_spaceship_group.add(my_spaceship)

def draw_bg():
    """
    Vẽ nền cuộn.
    Hàm này vẽ nền cuộn và cập nhật vị trí của nó để tạo ảo giác cuộn liên tục.
    """
    global bg_y1, bg_y2
    screen.blit(bg, (0, bg_y1))
    screen.blit(bg, (0, bg_y2))
    bg_y1 += scroll_speed
    bg_y2 += scroll_speed
    if bg_y1 >= HEIGHT:
        bg_y1 = -bg_height
    if bg_y2 >= HEIGHT:
        bg_y2 = -bg_height

def draw_text(surf, text, size, x, y):
    """
    Vẽ chữ lên màn hình.
    Tham số:
        surf: Đối tượng pygame.Surface đại diện cho bề mặt để vẽ chữ lên.
        text: Chuỗi ký tự đại diện cho chữ sẽ được vẽ.
        size: Số nguyên đại diện cho kích thước phông chữ.
        x: Số nguyên đại diện cho tọa độ x của chữ.
        y: Số nguyên đại diện cho tọa độ y của chữ.
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_score(surf, text, size, x, y):
    """
    Vẽ điểm lên màn hình.
    Tham số:
        surf: Đối tượng pygame.Surface đại diện cho bề mặt để vẽ điểm lên.
        text: Chuỗi ký tự đại diện cho điểm sẽ được vẽ.
        size: Số nguyên đại diện cho kích thước phông chữ.
        x: Số nguyên đại diện cho tọa độ x của điểm.
        y: Số nguyên đại diện cho tọa độ y của điểm.
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)

def main_menu():
    """
    Hiển thị menu chính và xử lý đầu vào của người dùng.
    Hàm này hiển thị menu chính với các tùy chọn để bắt đầu trò chơi hoặc thoát. Nó cũng xử lý đầu vào của người dùng để bắt đầu trò chơi hoặc thoát ứng dụng.
    """
    global screen

    menu_song = pygame.mixer.music.load(os.path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(1)

    title = pygame.image.load(os.path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT))
    screen.blit(title, (0, 0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH / 2, HEIGHT / 2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH / 2, (HEIGHT / 2) + 40)
            pygame.display.update()

    ready = pygame.mixer.Sound(os.path.join(sound_folder, 'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "GET READY!", 40, WIDTH / 2, HEIGHT / 2)
    pygame.display.update()
    pygame.time.wait(2000)

# Create enemies
def create_enemies():
    """
    Tạo kẻ thù.
    Hàm này tạo ra một mạng lưới kẻ thù theo hàng và cột được xác định bởi các biến `rows` và `cols`.
    """
    for row in range(rows):
        for item in range(cols):
            enemy = Spaceship_enemys(100 + item * 100, 100 + row * 70, img_dir)
            Spaceship_enemys_group.add(enemy)


create_enemies()

# Display main menu
main_menu()

# Main loop
run = True
while run:
    clock.tick(FPS)

    draw_bg()

    # create random enemy bullet
    time_now = pygame.time.get_ticks()
    if time_now - last_enemy_bullet > enemy_cooldown:
        if Spaceship_enemys_group:  # check if there are any enemies
            attacking_enemy = random.choice(Spaceship_enemys_group.sprites())
            enemy_bullet = Enemy_Bullets(attacking_enemy.rect.centerx, attacking_enemy.rect.bottom, img_dir, my_spaceship_group, explosion_group, sound_folder)
            enemy_bullet_group.add(enemy_bullet)
            last_enemy_bullet = time_now

    if len(Spaceship_enemys_group) == 0:
        game_over = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if game_over == 0:
        game_over = my_spaceship.update(bullet_group, screen, explosion_group, img_dir, score)
        for bullet in bullet_group:
            score += bullet.update(Spaceship_enemys_group, explosion_group, score)
        Spaceship_enemys_group.update()
        enemy_bullet_group.update()
        explosion_group.update()
        if pygame.sprite.spritecollide(my_spaceship, Spaceship_enemys_group, True, pygame.sprite.collide_mask):
            my_spaceship.health_remaining -= 1
            explosion = Explosion(my_spaceship.rect.centerx, my_spaceship.rect.centery, 2, img_dir)
            explosion_group.add(explosion)
            explosion2_fx = pygame.mixer.Sound(os.path.join(sound_folder, 'explosion2.ogg'))
            explosion2_fx.play()
            score += 10
            if my_spaceship.health_remaining <= 0:
                game_over = -1
                explosion = Explosion(my_spaceship.rect.centerx, my_spaceship.rect.centery, 3, img_dir)
                explosion_group.add(explosion)

    else:
        if game_over == -1:
            draw_text(screen, "YOU LOSE!", 40, WIDTH / 2, HEIGHT / 2)
        if game_over == 1:
            draw_text(screen, "YOU WIN!", 40, WIDTH / 2, HEIGHT / 2)

    # Draw
    my_spaceship_group.draw(screen)
    bullet_group.draw(screen)
    Spaceship_enemys_group.draw(screen)
    enemy_bullet_group.draw(screen)
    explosion_group.draw(screen)

    # Draw score
    draw_score(screen, f"Score: {score}", 30, 10, 10)

    pygame.display.update()

pygame.quit()

