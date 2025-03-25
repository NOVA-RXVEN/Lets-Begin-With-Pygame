import pygame

pygame.init()

white = (255, 255, 255)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Image")

image = pygame.image.load("HALL.jpeg")
SIZE = (300, 300)

image = pygame.transform.scale(image, SIZE)
POSITION = (100,100)

while True: 
    
    display_surface.fill(white)
    display_surface.blit(image, POSITION)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    clock.tick(90)
    