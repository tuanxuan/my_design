import pygame

class Father_Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        """
        Khởi tạo đối tượng tàu vũ trụ.

        Tham số:
            x (int): Tọa độ x ban đầu của tàu vũ trụ.
            y (int): Tọa độ y ban đầu của tàu vũ trụ.
            image (pygame.Surface): Hình ảnh đại diện cho tàu vũ trụ.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        """
        Cập nhật vị trí của tàu vũ trụ.

        Tàu vũ trụ sẽ di chuyển sang phải và sau đó quay đầu và di chuyển sang trái
        """
        self.rect.x += 1 * self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 80:
            self.move_direction *= -1
            self.move_counter *= self.move_direction

help(Father_Spaceship.__init__)
help(Father_Spaceship.update)