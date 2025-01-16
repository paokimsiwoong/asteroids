import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        # 운석이 총알과 부딪혔을 때 실행 
        self.kill()
        # 기존 것은 삭제하고 새로 생성하므로 kill 실행

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            # 최소 크기면 두개로 조각나는 대신 사라지므로 바로 함수 종료
        
        spawn_angle = random.uniform(20, 50)
        # 새로 쪼개지는 운석의 속도 방향에 랜덤성 줄 때 사용할 값

        vel_1 = self.velocity.rotate(spawn_angle)
        vel_2 = self.velocity.rotate(-spawn_angle)
        # 새 운석들의 속도 벡터들

        spawn_radius = self.radius - ASTEROID_MIN_RADIUS
        # 새 운석은 기존 운석보다 ASTEROID_MIN_RADIUS만큼 작게

        spawn_1 = Asteroid(self.position.x, self.position.y, spawn_radius)
        spawn_1.velocity = vel_1 * 1.2
        spawn_2 = Asteroid(self.position.x, self.position.y, spawn_radius)
        spawn_2.velocity = vel_2 * 1.2
        # 새 운석 객체들 생성 및 속도 할당


    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
        # 운석 그리기
    
    def update(self, dt):
        self.position += self.velocity * dt
        # 매 프레임 마다 속도 벡터 방향으로 이동