import pygame
from sys import exit
pygame.init()

icon = pygame.image.load("images/th.png")
screen_icon = pygame.display.set_icon(icon)
screen = pygame.display.set_mode((720,360))
screen_title = pygame.display.set_caption("The Blade Runner")
screen_clock = pygame.time.Clock()
screen_active = "Start"

game_text = pygame.font.Font("freesansbold.ttf",20)

background_sky = pygame.image.load("images/background/Sky.png")
background_ground = pygame.image.load("images/background/ground.png")

snail = pygame.image.load("images/snail/snail1.png")
snail_rect = snail.get_rect()
snail_rect.bottom = 300
snail_rect.right  = 720

player = pygame.image.load("images/player/player_stand.png").convert_alpha()
player_size = pygame.transform.scale2x(player)
player_rect = player.get_rect(midbottom = (80,300))
player_size_rect = player_size.get_rect(center = (360,180))
player_gravity = 0

score = 0

start_screen = pygame.image.load("images/blade.png")
start_rect = start_screen.get_rect(center = (360,180))

game_music = pygame.mixer.Sound("soundtrack/music.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :   
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -21
                screen_active = "Active"

            elif event.key == pygame.K_r and screen_active == "Deactive":
                snail_rect.right = 720
                score = 0
                screen_active = "Active"

    if screen_active == "Start":
        start_title = game_text.render("The Blade Runner",False,(64,64,64))
        start_text = game_text.render("Press 'Space' For Start",False,(64,64,64))
        start_title_rect = start_title.get_rect(midtop = (360,300))
        start_text_rect = start_text.get_rect(midtop = (360,330))
        screen.blit(start_screen,start_rect)
        screen.blit(start_title,start_title_rect)
        screen.blit(start_text,start_text_rect)

    elif screen_active == "Active":

        score_render = game_text.render(str(score),False,(64,64,64))
        score_rect = score_render.get_rect(center = (360,20))

        game_music.set_volume(0.5)
        game_music.play()

        snail_rect.left -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 720
            score += 1 
            
        elif player_rect.colliderect(snail_rect):
            screen_active = "Deactive"
        
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(background_sky,(0,0))
        screen.blit(background_ground,(0,300))
        screen.blit(score_render,score_rect)
        screen.blit(snail,snail_rect)
        screen.blit(player,player_rect)
        
    elif screen_active == "Deactive":
        game_mess_render = game_text.render(f"Your Score: {score}", False,(64,64,64))
        game_mess_1_render = game_text.render("Press 'R' For Restart ",False,(64,64,64))
        game_mess_rect = game_mess_render.get_rect(center = (360,300))
        game_mess_1_rect = game_mess_1_render.get_rect(center = (360,330))

        game_music.stop()

        screen.fill((94,124,162))
        screen.blit(player_size,player_size_rect)
        screen.blit(game_mess_render,game_mess_rect)
        screen.blit(game_mess_1_render,game_mess_1_rect)
    
    pygame.display.update()
    screen_clock.tick(60)
                