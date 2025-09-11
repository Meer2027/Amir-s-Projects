import pygame
import random
import time
#Group 18
#mousemotion - if the user has moved the mouse inside the Display
pygame.init()
Clock=pygame.time.Clock()
Screen=pygame.display.set_mode((800,800))
Starttime=time.time()
#screen = pygame.display.set_mode((800,800))
# rect(x position, y position, length , width)
#rect1.move( x - movement, y-movement)
#basket to hold candies
hold = pygame.Rect(300,700,80,20)
bucket = pygame.image.load('bucket_2fixed.png').convert_alpha()
pumpkin = pygame.transform.scale(bucket,(100,100))
basket = pygame.Surface((hold.w,hold.h))
score = 0

Backgroundrect = pygame.Rect(0,0,800,800)

#Instructions image
Instructions = pygame.image.load('Instructions_updated.png').convert_alpha()
Instructions1 = pygame.transform.scale(Instructions,(800,800))

#Background image
Background = pygame.image.load('Spooky background.jpeg').convert_alpha()
Background1 = pygame.transform.scale(Background,(800,800))

#game sound
game_music = pygame.mixer.Sound('mixkit-game-level-music-689.wav')
pointup = pygame.mixer.Sound('mixkit-winning-a-coin-video-game-2069.wav')
losing = pygame.mixer.Sound('Losing-sound-effect.mp3')

#Timer
Font = pygame.font.Font(None, 36)
def draw_text(text, color, x, y):

    screentext = Font.render(text, True, color)
    Screen.blit(screentext, (x, y))


start_candies = False
black_screen = False
game_over_screen = pygame.image.load('Fallout-death-2.webp').convert_alpha()
game_over = pygame.transform.scale(game_over_screen,(800,800))
def candy_jackpot():
    #random candies
    candy_basket = random.choice(['Skittles', 'M&M', 'Kit-Kat', 'Hershey', 'ButterFingers'])
    spawn_side = random.randint(0,800-20)
    if candy_basket == 'Skittles':
        wrapped_candy = pygame.image.load('Candy2-Fixed.png').convert_alpha()
        candy_corn1 = pygame.transform.scale(wrapped_candy,(40,40))
        candy = pygame.Rect(spawn_side,0,20,20)
        candy_speed = [0, 2]
    elif candy_basket == 'M&M':
        wrapped_candy = pygame.image.load('Candy_1.png').convert_alpha()
        candy_corn1 = pygame.transform.scale(wrapped_candy, (40, 40))
        candy = pygame.Rect(spawn_side, 0, 20, 20)
        candy_speed = [0, 2]
    elif candy_basket == 'Kit-Kat':
        wrapped_candy = pygame.image.load('Candy5-fixed.png').convert_alpha()
        candy_corn1 = pygame.transform.scale(wrapped_candy, (40,40))
        candy = pygame.Rect(spawn_side, 0, 20, 20)
        candy_speed = [0, 2]
    elif candy_basket == 'Hershey':
        wrapped_candy = pygame.image.load('Candy3-fixed.png').convert_alpha()
        candy_corn1 = pygame.transform.scale(wrapped_candy, (40,40))
        candy = pygame.Rect(spawn_side, 0, 20, 20)
        candy_speed = [0, 2]
    elif candy_basket == 'ButterFingers':
        wrapped_candy = pygame.image.load('Candy4-fixed.png').convert_alpha()
        candy_corn1 = pygame.transform.scale(wrapped_candy, (40,40))
        candy = pygame.Rect(spawn_side, 0, 20, 20)
        candy_speed = [0, 2]
    wrapped_candyRect = candy_corn1.get_rect()
    wrapped_candyRect.x = random.randint(40, 760)
    return wrapped_candyRect,candy_speed, candy_corn1, candy
candy_belt = []
# max candies on the screen
max_candies = 5
spawn_rate = 1000
spawn_time = pygame.time.get_ticks()
rand_color = random.randint(1,255)




running = True
Background_current = Instructions1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # controls for basket
    keys = pygame.key.get_pressed()

    Screen.blit(Background_current, Backgroundrect)

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        hold.move_ip(-8, 0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        hold.move_ip(8, 0)
    if hold.x < 0:
        hold.x = 0
    if hold.x > 740:
        hold.x = 740
    if keys[pygame.K_1]:
        Background_current = Instructions1
        start_candies = False
        game_music.stop()
    if keys[pygame.K_2]:
        Background_current = Background1
        Starttime = time.time()
        start_candies = True
    if start_candies:
        # collusions and resetting of candies
        game_music.play()
        for i in range(len(candy_belt)):
            wrapped_candyRect, candy_speed, candy_corn1, candy  = candy_belt[i]
            wrapped_candyRect.y += candy_speed[1]
            if (wrapped_candyRect.x < -wrapped_candyRect.w or wrapped_candyRect.x > 800):
                candy_belt[i] = candy_jackpot()
            elif hold.colliderect(wrapped_candyRect):
                candy_belt[i] = candy_jackpot()
                score += 1
                game_music.stop()
                pointup.play()
                game_music.play()
            elif wrapped_candyRect.y < -wrapped_candyRect.h or wrapped_candyRect.y > 800:
                start_candies = False
                black_screen = True


                #running = False
                print("game over!")
                print(score)
                game_music.stop()
                losing.play()
            #    replace with game over screen
            else:
                wrapper = pygame.Surface((wrapped_candyRect.w, wrapped_candyRect.h))

                Screen.blit(candy_corn1, (wrapped_candyRect.x, wrapped_candyRect.y))
        basket.fill((255, 255, 255))
        Screen.blit(pumpkin, (hold.x, hold.y))
        # spawning time between candines
        current_time = pygame.time.get_ticks()
        if current_time - spawn_time > spawn_rate and len(candy_belt) < max_candies:
            wrapped_candyRect, candy_speed, candy_corn1 , candy = candy_jackpot()
            candy_belt.append(candy_jackpot())
            spawn_time = current_time

    if keys[pygame.K_ESCAPE]:
        running=False
        print("Congrats!")
        print(score)

    # blitting timer/background


    elaspedtime = round(time.time() - Starttime, 2)

    if Background_current == Background1:
        draw_text("Time:" + str(elaspedtime) + "s", (255, 255, 255), 10, 10)

    if elaspedtime >= 60:
        Screen.fill((0,0,0))
        draw_text("Congrats you win",(255,255,255),350,350)
        draw_text("Press esc when you want to exit", (255, 255, 255), 350, 600)

    if black_screen == True:
        Screen.blit(game_over, Backgroundrect)
        draw_text("Sorry You lost", (255, 255, 255), 300, 350)
        draw_text("Your score was " + str(score), (255, 255, 255), 300, 400)












    pygame.display.flip()
    Clock.tick(60)
