import pygame
import os
import random
from fatherspaceship import Father_Spaceship

class Spaceship_enemys(Father_Spaceship):
    def __init__(self, x, y, img_dir):
        """
        Khởi tạo đối tượng tàu vũ trụ của kẻ địch.

        Tham số:
            x (int): Tọa độ x của tàu vũ trụ.
            y (int): Tọa độ y của tàu vũ trụ.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
        """
        image = pygame.image.load(os.path.join(img_dir, 'enemy' + str(random.randint(1, 5)) + '.png')).convert_alpha()
        super().__init__(x, y, image)



help(Spaceship_enemys.__init__)