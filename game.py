#speed game
#v0.2
#by python-nerd1235
F_V=0.2
import pygame
import json
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    with open("level.json", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("failed to find level.json")
    sys.exit()
try:
    blocks=data["B"]
    end=[450,0]
    #boom boom earth die if bad format
    if data["F"]!=f"FORMAT {F_V}":3/0
    
except:
    print("Bad format in level.json")
    sys.exit()
pygame.init()
text_font = pygame.font.SysFont('Arial', 15)
running = True
x=0
wIn=True
y=400
time=0
win = pygame.display.set_mode((500, 500))
win.fill((255, 0, 0))
text=text_font.render(f"GET REDY!", True, (255, 255, 255))
win.blit(text, (200, 200))
pygame.display.update()
pygame.time.wait(1000)
win.fill((255, 0, 0))
text=text_font.render(f"GO!", True, (255, 255, 255))
win.blit(text, (200, 200))
pygame.display.update()
pygame.time.wait(100)
while running:
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (0, 450, 500, 50))
    pygame.draw.rect(win, (255, 0, 255), (x, y, 50, 50))
    pygame.draw.rect(win, (0, 255, 0), (end[0], end[1], 50, 50))
    text=text_font.render(f'time: {time}', True, (0, 0, 255))
    for i in blocks:
        pygame.draw.rect(win, (255, 0, 0), (i[0], i[1], 50, 50))
    win.blit(text, (30, 470))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y>0:
        y-=50
    if keys[pygame.K_DOWN] and y<400:
        y+=50
    if keys[pygame.K_LEFT] and x>0:
        x-=50
    if keys[pygame.K_RIGHT] and x<450:
        x+=50
    if [x, y] in blocks:
        wIn=False
        running = False
    if [x, y]==end:
        running = False
    pygame.display.update()
    time+=1
    pygame.time.Clock().tick(30)
if wIn:
        win.fill((0, 0, 0))
        text=text_font.render(f"YOU WIN! TIME: {time}", True, (255, 255, 255))
        win.blit(text, (200, 200))
        pygame.display.update()
        pygame.time.wait(1500)
        running = False
else:
        win.fill((255, 0, 0))
        text=text_font.render(f"YOU DIED.", True, (255, 255, 255))
        win.blit(text, (200, 200))
        pygame.display.update()
        pygame.time.wait(1000)
        running = False
pygame.quit()
