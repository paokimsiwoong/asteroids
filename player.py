import pygame
import circleshape
from constants import PLAYER_RADIUS

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        # PLAYER_RADIUS는 20
        # 플레이어 클래스는 겉으로는 삼각형으로 보이지만 충돌 판정은 원으로
        # => CircleShape 상속

        self.rotation = 0
    
    def triangle(self):
        # 플레이어 중심점(현재 위치) self.position(pygame.Vector2(x,y))에서 
        # self.rotation 값으로 삼각형 3 꼭지점 좌표 계산
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # (0,1) 벡터(크기1)을 현재 rotation 값만큼 회전 시키면 우주선 앞방향 크기 1 벡터가 된다
        # @@@@ 게임에선 y축이 반대 (밑 방향이 양수)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        # forward와 수직인 오른쪽 방향 벡터

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)
        # surface 인수에 주어진 스크린에 색 color, 두께 width인 다각형을 그린다
        # 다각형의 꼭지점들의 좌표는 points에서 입력