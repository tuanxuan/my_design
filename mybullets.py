import pygame
import os
from fatherbullets import Father_Bullets
from explosion import Explosion

class Bullets(Father_Bullets):
    def __init__(self, x, y, img_dir, sound_folder):
        """
        Khởi tạo đối tượng đạn của người chơi.

        Tham số:
            x (int): Tọa độ x ban đầu của đạn.
            y (int): Tọa độ y ban đầu của đạn.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
            sound_folder (str): Đường dẫn đến thư mục chứa âm thanh.
        """
        image = pygame.image.load(os.path.join(img_dir, 'bullet.png')).convert_alpha()
        super().__init__(x, y, image)
        self.img_dir = img_dir
        self.sound_folder = sound_folder

    def update(self, Spaceship_enemys_group, explosion_group, score):
        """
        Cập nhật vị trí của đạn và xử lý va chạm với tàu vũ trụ của kẻ địch.

        Tham số:
            Spaceship_enemys_group (pygame.sprite.Group): Nhóm chứa tàu vũ trụ của kẻ địch.
            explosion_group (pygame.sprite.Group): Nhóm chứa hiệu ứng nổ.
            score (int): Điểm số hiện tại.

        Returns:
            int: Số điểm được thêm vào sau khi va chạm.
        """
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, Spaceship_enemys_group, True, pygame.sprite.collide_mask):
            self.kill()
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3, self.img_dir)
            explosion_group.add(explosion)
            explosion_fx = pygame.mixer.Sound(os.path.join(self.sound_folder, 'explosion.ogg'))
            explosion_fx.play()
            return 10
        return 0


help(Bullets.__init__)
help(Bullets.update)