import pygame
import os

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size, img_dir):
        """
        Khởi tạo hiệu ứng nổ.

        Tham số:
            x (int): Tọa độ x của hiệu ứng nổ.
            y (int): Tọa độ y của hiệu ứng nổ.
            size (int): Kích thước của hiệu ứng nổ.
            img_dir (str): Đường dẫn đến thư mục chứa hình ảnh.
        """
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(os.path.join(img_dir, f'explosion{num}.png')).convert_alpha()
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        """
        Cập nhật hiệu ứng nổ.

        Hiệu ứng nổ sẽ thay đổi hình ảnh của nó theo một tốc độ nhất định,
        cho đến khi hình ảnh cuối cùng được hiển thị, sau đó hiệu ứng sẽ bị xóa khỏi nhóm sprite.
        """
        explosion_speed = 3
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


help(Explosion.__init__)
help(Explosion.update)