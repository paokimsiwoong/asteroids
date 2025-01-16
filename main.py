import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

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
        pygame.display.flip()
        # 화면 리프레쉬
        dt = clock.tick(framerate=60) / 1000
        # pygame.time.Clock().tick()
        # 틱 함수는 각 프레임마다 불리면서 이전 호출로부터 얼마나 시간이 흘렀는지 계산한다
        # framerate 인수(optional)을 주면 주어진 frame rate에 맞게 기다리게 해서 fps 조절 가능
        # 또 경과시간을 반환하므로(millisec) 그 경과시간을 dt에 저장(sec로 변환)

if __name__ == "__main__":
    main()