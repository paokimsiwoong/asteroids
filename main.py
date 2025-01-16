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

if __name__ == "__main__":
    main()