import pygame

pygame.init()

beige = (238, 223, 201)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((500,500))

pygame.display.set_caption("Image")

image = pygame.image.load("Weeknd.png")
SIZE = (400, 400)

image = pygame.transform.scale(image, SIZE)
POSITION = (50, 50)

while True: 
    
    display_surface.fill(beige)
    display_surface.blit(image, POSITION)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    clock.tick(90)
    