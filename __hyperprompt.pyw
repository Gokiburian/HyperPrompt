import pygame
import win32gui
import subprocess
import sys

KEY_DICT = {pygame.K_e: 'e.bat', pygame.K_c: 'c.bat'}
BACK_COLOR = (0, 0, 0)
TEXT_COLOR = (155, 155, 155)
FONT_SIZE = 30
WIDTH = 200
HEIGHT = 60
PLAY_SOUND = True


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("HyperPrompt")
wm_info = pygame.display.get_wm_info()
handle = wm_info["window"]
win32gui.MoveWindow(handle, 0, 0, WIDTH, HEIGHT, 1)
clock = pygame.time.Clock()
FPS = 10
font = pygame.font.Font(pygame.font.match_font("yumincho"), FONT_SIZE)
sound = pygame.mixer.Sound("_se.wav")


def main():
    screen.fill(BACK_COLOR)
    screen.blit(font.render("HyperPrompt", True, TEXT_COLOR), (10, (HEIGHT-FONT_SIZE)//2))
    pygame.display.update()

    while True:
        clock.tick(FPS)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            for key in KEY_DICT:
                if event.key == key:
                    if PLAY_SOUND:
                        sound.play()
                    subprocess.Popen(KEY_DICT[key], shell=True)


if __name__ == "__main__":
    main()
