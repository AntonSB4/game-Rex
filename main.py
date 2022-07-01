import pygame

pygame.init()

display_width = 600
display_height = 800

display = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('Run Rex! run!')

icon = pygame.image.load("rex.png")
pygame.display.set_icon(icon)


class Cactus:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            pygame.draw.rect(display, (200, 150, 70), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
        else:
            self.x = display_width + 200


# User
usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 300

# Barrier
cactus_width = 20
cactus_height = 70
cactus_x = display_width + 200
cactus_y = display_height - cactus_height - 300

clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


def run_game():
    global make_jump
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        display.fill((255, 255, 255))

        draw_array(cactus_arr)

        pygame.draw.rect(display, (0, 255, 0), (usr_x, usr_y, usr_width, usr_height))

        pygame.display.update()
        clock.tick(80)


def jump():
    global usr_y, make_jump, jump_counter
    if jump_counter >= - 30:
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    array.append(Cactus(display_width + 20, display_width - 170, 20, 70, 5))
    array.append(Cactus(display_width + 30, display_width - 150, 30, 50, 5))
    array.append(Cactus(display_width + 600, display_width - 180, 25, 80, 5))


def draw_array(array):
    for cactus in array:
        cactus.move()


run_game()
