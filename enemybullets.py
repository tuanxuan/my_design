import pygame
import os
from fatherbullets import Father_Bullets
from explosion import Explosion


class Enemy_Bullets(Father_Bullets):
    def __init__(self, x, y, img_dir, my_spaceship_group, explosion_group, sound_folder):
        """
        Khởi tạo đối tượng đạn của kẻ địch.

        Tham số:
            x (int): Tọa độ x của đạn.
            y (int): Tọa độ y của đạn.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
            my_spaceship_group (pygame.sprite.Group): Nhóm chứa tàu vũ trụ của người chơi.
            explosion_group (pygame.sprite.Group): Nhóm chứa hiệu ứng nổ.
            sound_folder (str): Đường dẫn đến thư mục chứa âm thanh.
        """
        image = pygame.image.load(os.path.join(img_dir, 'enemy_bullet.png')).convert_alpha()
        super().__init__(x, y, image)
        self.my_spaceship_group = my_spaceship_group
        self.explosion_group = explosion_group
        self.img_dir = img_dir
        self.sound_folder = sound_folder

    def update(self):
        """
        Cập nhật vị trí của đạn và kiểm tra va chạm với tàu vũ trụ của người chơi.
        """
        self.rect.y += 2
        if self.rect.top > 800:
            self.kill()
        if pygame.sprite.spritecollide(self, self.my_spaceship_group, False, pygame.sprite.collide_mask):
            self.kill()
            my_spaceship = self.my_spaceship_group.sprites()[0]  # giả sử chỉ có một tàu vũ trụ
            my_spaceship.health_remaining -= 1
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2, self.img_dir)
            self.explosion_group.add(explosion)
            explosion2_fx = pygame.mixer.Sound(os.path.join(self.sound_folder, 'explosion2.ogg'))
            explosion2_fx.play()



help(Enemy_Bullets.__init__)
help(Enemy_Bullets.update)