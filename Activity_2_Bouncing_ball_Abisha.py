import pygame

pygame.init()
red=(255,0,0)
black=(0,0,0)
y=150.0
vel=1
window = pygame.display.set_mode((300,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    window.fill(black)
    pygame.draw.circle(window, red, (150,y), 15)
    
    pygame.display.update()
    y+=vel
    pygame.time.delay(15)
    if y>280 or y<15:
        vel=vel*-1
    

