import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    # pygame 모듈 초기화
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # GUI 창(window)을 screen에 할당 screen은 pygame.Surface 오브젝트
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    # 시간 경과 등을 추적하는데 사용가능한 Clock 오브젝트 생성
    dt = 0
    # 루프 안에서 프레임 당 경과시간을 저장할 변수

    updatable = pygame.sprite.Group()
    # 각 프레임마다 update가 실행되어야 하는 오브젝트들을 담을 그룹
    drawable = pygame.sprite.Group()
    # 각 프레임마다 draw가 실행되어야 하는 오브젝트들을 담을 그룹
    asteroids = pygame.sprite.Group()
    # 운석 객체들을 담을 그룹

    Player.containers = (updatable, drawable)
    # Player 클래스 변수 containers에 (updatable, drawable) 할당
    # ===> 모든 플레이어 인스턴스들은 위 두 그룹에 속하게 된다

    Asteroid.containers = (asteroids, updatable, drawable)
    # Asteroid 클래스는 추가로 asteroids 그룹에도 속한다

    AsteroidField.containers = (updatable)
    # AsteroidField 클래스는 따로 그려지지 않으므로 updatable 그룹에만 속한다
    # update 함수로 시간을 체크해 스폰 쿨타임마다 운석 생성

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    # Player 오브젝트 생성

    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 유저가 gui창을 닫았을 경우 루프를 종료하게하는 코드
            
        screen.fill(color=(0,0,0))
        # pygame.Surface.fill() 함수
        # color에 RGB 또는 RGBA 값을 tuple형태로 입력
        # 화면을 검정색으로 칠하기
        # 단순히 color="black" 입력도 가능

        for obj in updatable:
            obj.update(dt)
            # updatable 그룹에 속한 모든 오브젝트들 update 함수 실행

        for obj in drawable:
            obj.draw(screen)
            # drawable 그룹에 속한 모든 오브젝트들 draw 함수 실행

        pygame.display.flip()
        # 화면 리프레쉬
        dt = clock.tick(60) / 1000
        # tick 안에 framerate=60 입력하니 TypeError: Clock.tick() takes no keyword arguments????
        # pygame.time.Clock().tick()
        # 틱 함수는 각 프레임마다 불리면서 이전 호출로부터 얼마나 시간이 흘렀는지 계산한다
        # framerate 인수(optional)을 주면 주어진 frame rate에 맞게 기다리게 해서 fps 조절 가능
        # 또 경과시간을 반환하므로(millisec) 그 경과시간을 dt에 저장(sec로 변환)

if __name__ == "__main__":
    main()