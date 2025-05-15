import pygame
import settings


class main():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(settings.screen_resolution)
        self.running=True



    def run(self):
        while self.running:
            self.screen.fill((255,255,255))
            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False







if __name__ == "__main__":
    JD : main = main()

    JD.run()

    del JD