import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
        # 운석 그리기
    
    def update(self, dt):
        self.position += self.velocity * dt
        # 매 프레임 마다 속도 벡터 방향으로 이동