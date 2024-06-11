import pygame

class Father_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        """
        Khởi tạo đối tượng đạn.

        Tham số:
            x (int): Tọa độ x ban đầu của đạn.
            y (int): Tọa độ y ban đầu của đạn.
            image (pygame.Surface): Hình ảnh đại diện cho đạn.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        """
        Cập nhật vị trí của đạn và xóa nó khỏi nhóm sprite nếu đạn ra khỏi màn hình.

        Nếu đạn di chuyển ra khỏi phạm vi màn hình theo chiều dọc, nó sẽ bị xóa khỏi nhóm sprite.
        """
        if self.rect.top < 0 or self.rect.bottom > 800:  # Sử dụng 800 thay vì chiều cao của màn hình
            self.kill()


help(Father_Bullets.__init__)
help(Father_Bullets.update)