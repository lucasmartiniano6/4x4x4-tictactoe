import pygame

pygame.init()
width=700
height=600
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('clicked on image')

x = 20; # x coordnate of image
y = 30; # y coordinate of image

squares = [pygame.image.load("square.png").convert() for _ in range(4)]
for _ in range(4):
  for idx in range(4):
    screen.blit(squares[idx], (x,y)) # paint to screen
    pygame.display.flip() # paint screen one time
    x += 70
  y += 70
  x = 20

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            for idx in range(4):
              if squares[idx].get_rect().collidepoint(x, y):
                  print('clicked on', idx)
              
#loop over, quite pygame
pygame.quit()
