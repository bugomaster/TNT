from glob import glob
import pygame
from scipy.ndimage.interpolation import zoom
import random
import numpy as np
import sys

from soupsieve import closest
from sqlalchemy import false
pygame.init()
isneg = False
number15 = 969
name = f"world{random.randint(0,1000)}.txt"
f = open(name, "x")
for ds in range(0, 1000):

    for d in range(0, 1000):
        f.write('0')
    f.write('\n')


def writetoline(filename, y, x, line):
    a_file = open(filename, "r")
    list_of_lines = a_file.readlines()

    list_of_lines[x] = list_of_lines[x][0:y] + \
        (line) + list_of_lines[x][y+len(line):]

    a_file = open(filename, "w")
    a_file.writelines(list_of_lines)
    a_file.close()


def is_new_Chunk_needed(number):
    global isneg
    global number15
    number15 = 969
    if not keyStates[1] and keyStates[0]:
        number += 8
    if not keyStates[1] and keyStates[2]:
        number -= 8
    if not keyStates[1] and keyStates[3]:
        number += 8

    while 1:

        isneg = number15 - number < 0
        if abs(number15 - number) < 16:
            return True
        if number15 < 0:
            return False
        number15 -= 32


def find_upper(number):
    number15 = 969
    while 1:

        if (number15 - number < 0 and number15 - number > -32) or number15 == number:
            return number15
        if number15 < 0:
            break
        number15 -= 31


def write_perlin_32x32_POS(x, z):

    np.set_printoptions(threshold=sys.maxsize)
    arr = np.random.uniform(size=(4, 4))
    arr = zoom(arr, 8)
    arr = arr > 0.5
    arr = np.where(arr, '0', '1')
    arr = np.array_str(arr, max_line_width=500)
    strg = ""
    for shit in arr:
        if shit == ']':
            dd = f"{strg}\n"
            x -= 32

            if len(dd) > 5:
                if x < 950 and z < 950:
                    writetoline(name, x, z, strg)
            strg = ""
            z += 1
        try:
            strg += f"{int(shit)}"
            if strg[len(strg)-2:] == "01":
                strg = f"{strg[:len(strg)-4]}221"
            if strg[len(strg)-2:] == "10":
                strg = f"{strg[:len(strg)-4]}122"
            x += 1

        except:
            pass


f.close


j = 0
i = 0

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
water = pygame.image.load('water.png').convert_alpha()
water = pygame.transform.scale(water, (50, 50))
grass = pygame.image.load('grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (50, 50))
sand = pygame.image.load('sand.png').convert_alpha()
sand = pygame.transform.scale(sand, (50, 50))

ashdown1 = pygame.image.load('pics/ashdown1.png').convert_alpha()
ashdown1 = pygame.transform.scale(ashdown1, (50, 50))
ashdown2 = pygame.image.load('pics/ashdown2.png').convert_alpha()
ashdown2 = pygame.transform.scale(ashdown2, (50, 50))
ashdown3 = pygame.image.load('pics/ashdown3.png').convert_alpha()
ashdown3 = pygame.transform.scale(ashdown3, (50, 50))

ashup1 = pygame.image.load('pics/ashup1.png').convert_alpha()
ashup1 = pygame.transform.scale(ashup1, (50, 50))
ashup2 = pygame.image.load('pics/ashup2.png').convert_alpha()
ashup2 = pygame.transform.scale(ashup2, (50, 50))
ashup3 = pygame.image.load('pics/ashup3.png').convert_alpha()
ashup3 = pygame.transform.scale(ashup3, (50, 50))

ashleft1 = pygame.image.load('pics/ashleft1.png').convert_alpha()
ashleft1 = pygame.transform.scale(ashleft1, (50, 50))
ashleft2 = pygame.image.load('pics/ashleft2.png').convert_alpha()
ashleft2 = pygame.transform.scale(ashleft2, (50, 50))
ashleft3 = pygame.image.load('pics/ashleft3.png').convert_alpha()
ashleft3 = pygame.transform.scale(ashleft3, (50, 50))

ashright1 = pygame.image.load('pics/ashright1.png').convert_alpha()
ashright1 = pygame.transform.scale(ashright1, (50, 50))
ashright2 = pygame.image.load('pics/ashright2.png').convert_alpha()
ashright2 = pygame.transform.scale(ashright2, (50, 50))
ashright3 = pygame.image.load('pics/ashright3.png').convert_alpha()
ashright3 = pygame.transform.scale(ashright3, (50, 50))


imgs_run = [[ashright1, ashright2], [ashleft1, ashleft2],
            [ashup1, ashup2], [ashdown1, ashdown2]]


#            right  left   up     down
keyStates = [False, False, False, False]
nig = 1
state = 0
j = 0
x = 400
z = 400
z_map = 425
mapstrings = []
x_map = 425
blocksdict = {"0": grass, "1": water, "2": sand}
position_perlin_already_there = {"425-425": True}
write_perlin_32x32_POS(425, 425)
speed = 1
gamespeed = 60
while 1:

    clock.tick(gamespeed)
    a_file = open(name)
    mapstrings = []

    if is_new_Chunk_needed(x_map):
        if isneg:

            try:
                if position_perlin_already_there[f"{number15}-{find_upper(z_map)}"]:
                    pass
            except:
                position_perlin_already_there[f"{number15}-{find_upper(z_map)}"] = True
                write_perlin_32x32_POS(number15, find_upper(z_map))

    if is_new_Chunk_needed(z_map):
        if isneg:

            try:
                if position_perlin_already_there[f"{number15}-{find_upper(x_map)}"]:
                    pass
            except:
                position_perlin_already_there[f"{number15}-{find_upper(x_map)}"] = True
                write_perlin_32x32_POS(number15, find_upper(x_map))

    for position, line in enumerate(a_file):
        k1 = (x_map)
        k2 = (x_map)+16
        k3 = int((z_map))
        k4 = int((z_map)+16)
        if position >= k1 and position < k2:
            mapstrings.append(
                line[k3:k4])
    a_file.close()

    if keyStates != [False, False, False, False]:

        onetimeonly = True
        for i1 in range(0, 16):
            for j1 in range(0, 16):
                x_0 = i1*50
                z_0 = j1*50
                if onetimeonly:
                    if (x_0, z_0) == (400, 400) and mapstrings[i1][j1] == '1':
                        gamespeed = 30
                        onetimeonly = False

                    else:
                        gamespeed = 60
                screen.blit(blocksdict[mapstrings[i1][j1]], (x_0, z_0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyStates = [False, False, False, False]
                j = 0
                nig = 1
                keyStates[1] = True
            if event.key == pygame.K_RIGHT:
                j = 0
                nig = 1
                keyStates = [False, False, False, False]

                keyStates[0] = True
            if event.key == pygame.K_UP:
                j = 0
                nig = 1
                keyStates = [False, False, False, False]

                keyStates[2] = True
            if event.key == pygame.K_DOWN:
                j = 0
                nig = 1
                keyStates = [False, False, False, False]

                keyStates[3] = True

            if event.type == pygame.QUIT:
                break
        if event.type == pygame.KEYUP:
            keyStates = [False, False, False, False]
            screen.blit(imgs_run[state][j], (x, z))

    if keyStates[0]:
        screen.blit(imgs_run[0][j], (x, z))
        x_map += speed
        state = 0
    elif keyStates[1]:
        screen.blit(imgs_run[1][j], (x, z))
        state = 1

        x_map -= speed

    elif keyStates[2]:
        screen.blit(imgs_run[2][j], (x, z))
        state = 2

        z_map -= speed

    elif keyStates[3]:
        screen.blit(imgs_run[3][j], (x, z))
        state = 3

        z_map += speed

    j += nig
    nig *= -1
    pygame.display.flip()

pygame.quit()
exit()
