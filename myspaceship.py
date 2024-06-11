import pygame
import os
from fatherspaceship import Father_Spaceship
from mybullets import Bullets
from explosion import Explosion

class My_spaceship(Father_Spaceship):
    def __init__(self, x, y, health, img_dir, sound_folder):
        """
        Khởi tạo đối tượng tàu vũ trụ của người chơi.

        Tham số:
            x (int): Tọa độ x ban đầu của tàu vũ trụ.
            y (int): Tọa độ y ban đầu của tàu vũ trụ.
            health (int): Mức máu ban đầu của tàu vũ trụ.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
            sound_folder (str): Đường dẫn đến thư mục chứa âm thanh.
        """
        image = pygame.image.load(os.path.join(img_dir, 'myspaceship1.png')).convert_alpha()
        super().__init__(x, y, image)
        self.sound_folder = sound_folder
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self, bullet_group, screen, explosion_group, img_dir, score):
        """
        Cập nhật trạng thái của tàu vũ trụ của người chơi.

        Tham số:
            bullet_group (pygame.sprite.Group): Nhóm chứa đạn của người chơi.
            screen (pygame.Surface): Màn hình game.
            explosion_group (pygame.sprite.Group): Nhóm chứa hiệu ứng nổ.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
            score (int): Điểm số hiện tại.

        Returns:
            int: Mã trạng thái kết thúc game.
        """
        speed = 7
        cooldown = 500
        game_over = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < 600:
            self.rect.x += speed
        if key[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= speed
        if key[pygame.K_DOWN] and self.rect.bottom < 800:
            self.rect.y += speed
        time_now = pygame.time.get_ticks()
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            laser_fx = pygame.mixer.Sound(os.path.join(self.sound_folder, 'laser.ogg'))
            laser_fx.play()
            bullet = Bullets(self.rect.centerx, self.rect.top, img_dir, self.sound_folder)
            bullet_group.add(bullet)
            self.last_shot = time_now
        self.mask = pygame.mask.from_surface(self.image)
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
        elif self.health_remaining <= 0:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3, img_dir)
            explosion_group.add(explosion)
            game_over = -1
        return game_over



help(My_spaceship.__init__)
help(My_spaceship.update)