import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [   # 왼쪽 벽 
            pygame.Vector2(1, 0), #=> 여기서 생성된 운석들은 (임의 값으로 방향 회전은 하지만) 오른쪽 방향(즉, 디스플레이 안쪽 방향) 속도 벡터를 가진다 
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), # 임의값 y를 받아 왼쪽 벽 모서리 위 한점 선택하는 함수
        ], 
        [   # 오른쪽 벽
            pygame.Vector2(-1, 0), # 왼쪽 벽과 반대
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ], 
        [   # 위쪽 벽
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [   # 아래쪽 벽
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        # 운석 생성 함수
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            # 지정된 ASTEROID_SPAWN_RATE(0.8초) 마다 임의 위치에 운석 생성
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            # 4개의 벽 중 하나 선택
            speed = random.randint(40, 100)
            # 운석 속도 랜덤 선택
            velocity = edge[0] * speed
            # edge[0]은 생성되는 벽 edge에 수직하면서 디스플레이 안쪽을 향하는 방향 벡터
            velocity = velocity.rotate(random.randint(-30, 30))
            # 모든 운석이 벽에 수직하게 움직이면 심심하므로 -30~30 랜덤 회전
            position = edge[1](random.uniform(0, 1))
            # edge[1]은 0~1 사이의 값을 받아 해당 벽 위의 한점을 반환(pygame.Vector2) 
            kind = random.randint(1, ASTEROID_KINDS)
            # ASTEROID_KINDS = 3 ==> 1~3 사이 값
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
            # 생성되는 운석의 radius는 1~3 * ASTEROID_MIN_RADIUS(20)