#speed game level maker.
#v0.1
#by python-nerd1235
import pygame
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def box(x,y,screen):
    pygame.draw.line(screen, (255, 255, 255), (x,y), (x, y+50), 3)
    pygame.draw.line(screen, (255, 255, 255), (x,y+50), (x+50, y+50), 3)
    pygame.draw.line(screen, (255, 255, 255), (x+50,y+50), (x+50, y), 3)
    pygame.draw.line(screen, (255, 255, 255), (x+50,y), (x, y), 3)
    return 0

blocks=[]
pygame.init()
run = True
win = pygame.display.set_mode((500, 500))
pos = [0,0]
while run:
    win.fill((0, 0, 0))
    for i in blocks:
        pygame.draw.rect(win, (255, 0, 0), (i[0], i[1], 50, 50))
    box(pos[0],pos[1],win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and pos[1] >= 50:
                pos[1] -= 50
            elif event.key == pygame.K_DOWN and pos[1] <= 400:
                pos[1] += 50
            elif event.key == pygame.K_RIGHT and pos[0] <= 400:
                pos[0] += 50
            elif event.key == pygame.K_LEFT and pos[0] >= 50:
                pos[0] -= 50
            elif event.key == pygame.K_SPACE and not pos in blocks:
                blocks.append(pos.copy())
            elif event.key == pygame.K_x and pos in blocks:
                blocks.remove(pos)

            
        pygame.display.update()
        pygame.time.Clock().tick(30)
pygame.quit()
data={
    "B":blocks,
    "F":"FORMAT 0.2"
    }
with open("level.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
