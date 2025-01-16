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

    def check_collision(self, other):
        # 충돌 판정 함수
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
        # 멤버 변수 position은 pygame.Vector2이고 이 클래스에는 멤버메소드 distance_to(pygame.Vector2)가 있어 거리 계산 가능

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass