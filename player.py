import pygame
import circleshape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

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
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # PLAYER_TURN_SPEED(300) * dt 만큼 회전

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # 우주선 진행방향 유닛벡터 생성

        self.position += forward * PLAYER_SPEED * dt
        # self.position에 우주선 진행방향 PLAYER_SPEED * dt 크기 벡터 더하기
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)
        # surface 인수에 주어진 스크린에 색 color, 두께 width인 다각형을 그린다
        # 다각형의 꼭지점들의 좌표는 points에서 입력

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # 플레이어 키 입력 여부를 bool로 담고 있는 시퀀스
        # 키 이름으로 indexing 접근 

        if keys[pygame.K_w]:
            # pygame.K_w => 키보드 w 키
            # 전진
            self.move(dt)
        if keys[pygame.K_s]:
            # pygame.K_s => 키보드 s 키
            # 후진
            self.move(-dt)
        if keys[pygame.K_a]:
            # pygame.K_a => 키보드 a 키
            # 왼쪽 회전
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # pygame.K_d => 키보드 d 키
            # 오른쪽 회전
            self.rotate(dt)