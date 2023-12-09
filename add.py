import pygame #библиотека
import pygame.freetype

#создание окна
pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("лохи на луне")
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

#подгрузка всех спрайтов
cactus_image = pygame.image.load('image/Sprite-0003.png')
cactus_image = pygame.transform.scale(cactus_image, (50, 100))
dino = pygame.image.load('image/Sprite.png')
dino = pygame.transform.scale(dino, (100, 100))
ground = pygame.image.load('image/алы.png')

#создание группы
ground_bro = pygame.sprite.Group()
cactus_bro = pygame.sprite.Group()

#тайминг, когда будут появляться припятствия
event_lox = pygame.USEREVENT
event_odsfsgegdmg = pygame.USEREVENT +1
pygame.time.set_timer(event_lox, 2000)
pygame.time.set_timer(event_odsfsgegdmg,6000)

#класс для динозавра
class nigga(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()
        if self.rect.colliderect(dinose.rect):
            dinose.game_status = "menu"



class popa(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()
            dinose.score +=1
#движение динозавра
class din():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.step = 5
        self.y = 0
        self.max_jump = 40
        self.in_jump = False
        self.score = 0
        self.game_status = "game"

#система прыжка
    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y += 1
                self.rect.y -= self.step
            elif self.y < self.max_jump * 2:
                self.y += 1
                self.rect.y += self.step
            else:
                self.in_jump = False
                self.y = False

#постоянное рисование
    def draw(self):
        screen.blit(self.image, self.rect)

#обьект
dinose = din(dino, (120, 400))


#системные приколы
running = True
while running:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            dinose.in_jump = True
        if event.type == event_lox:
            gf = nigga(ground, (900,450))
            ground_bro.draw(screen)
            ground_bro.update()
        if event.type == event_odsfsgegdmg:
            c = popa(cactus_image, (900, 450))
            cactus_bro.add(c)

#доп функции
    screen.fill((250, 250, 250))
    cactus_bro.update()
    cactus_bro.draw(screen)
    if dinose.game_status == "game":

        dinose.jump()
        dinose.draw()
        font.render_to(screen, (850, 50), str(dinose.score), (0, 0, 0))
    else:
        font.render_to(screen, (450 , 150) , "HAHAHAHAHAHAHAHAHAHAHHAAHAHAHHAHAHAHA", (0,0,0))
    pygame.display.flip()
    clock.tick(60)
