
import pygame
import random

x = pygame.init()

#colors
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

game_width = 1200
game_height = 600
#creating window
gameWindow = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('Game Window')
pygame.display.update()



#clock..
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)
def text_screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snk(gameWindow, color,snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [ x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        gameWindow.fill(green)
        text_screen("WELCOME!", blue, 500, 200)
        text_screen(" Press SPACEBAR to continue...", blue, 350, 300)

        pygame.display.update()
        clock.tick(30)


def gameloop():

    with open('highscore.txt','r') as file:
        highscore = file.read()


    # game variables
    exit_game = False
    game_over = False
    snake_x = 590
    snake_y = 290
    snake_size = 20
    fps = 10
    velocity_x = 0
    velocity_y = 0
    velocity = 15
    score = 0

    snk_list = []
    snk_length = 1

    food_x = random.randint(50, game_width - 50)
    food_y = random.randint(50, game_height - 50)


    while not exit_game:

        if game_over:
            text_screen("GAME OVER! Press ENTER to continue...",blue,100,250)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and velocity_x == 0:
                        velocity_x = velocity
                        velocity_y = 0

                    elif event.key == pygame.K_a and velocity_x == 0:
                        velocity_x = -velocity
                        velocity_y = 0

                    elif event.key == pygame.K_w and velocity_y == 0:
                        velocity_y = -velocity
                        velocity_x = 0

                    elif event.key == pygame.K_s and velocity_y == 0:
                        velocity_y = velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if snake_x > game_width or snake_x < 0 or snake_y > game_height or snake_y < 0:
                game_over = True

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(50, game_width - 50)
                food_y = random.randint(50, game_height - 50)
                snk_length += 1

                if score > int(highscore):
                    highscore = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            gameWindow.fill(green)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot_snk(gameWindow, black, snk_list, snake_size)
            text_screen('score :' + str(score) + '  HighScore : ' + str(highscore), red, 10, 10)
        pygame.display.update()

        clock.tick(fps)



welcome()