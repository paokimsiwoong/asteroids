import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            # containers는 인스턴스 변수가 아닌 클래스 변수(==> 모든 인스턴스들이 동일하게 공유)
            super().__init__(self.containers)
            # containers 클래스변수에 할당된 그룹들에 이 클래스의 인스턴스들이 속하게 된다
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass