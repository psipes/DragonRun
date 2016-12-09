__author__ = 'Patricia'

import pygame, mapLibrary, StaticItems
class DrawMaze:
    def __init__(self, maze, startx, starty):
        gridBox = StaticItems.MazeWall((300,300))
        gridX = gridBox.rect.right - gridBox.rect.left
        self.gridX = gridX
        gridY = gridBox.rect.bottom - gridBox.rect.top
        self.gridY = gridY
        self.startx = startx
        self.starty = starty


        self.maze = maze
        startx +=10
        starty +=175

    def mazeCoords (self):
        mazeBlocks = []
        wallCoords = []

        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == 'x':
                    wall = ((gridX * countx + startx, gridY * county +starty))
                    wallCoords.append(wall)
            county +=1
            countx = 0
        for element in wallCoords:
            wall = StaticItems.MazeWall(element)
            mazeBlocks.append(wall)

        allMazeBlocks = pygame.sprite.Group (mazeBlocks)
        return allMazeBlocks

    def openSpaces(self):
        openCoords = []
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == 'x':
                    open = ((gridX * countx + startx, gridY * county +starty))
                    openCoords.append(open)
            county +=1
            countx = 0
        return openCoords


    def playerStart(self):
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == 'P':
                    playerPos = ((gridX * countx + (gridX/2) + startx, gridY * county - (gridY/2) +starty))
            county +=1
            countx = 0
        return playerPos


    def breadcrumbCoords (self):
        crumbCoords = []
        crumbs = []
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == 'o':
                    breadCrumb = ((gridX * countx - (gridX/2) + startx, gridY * county - (gridY/2) + starty))
                    crumbCoords.append(breadCrumb)
            county +=1
            countx = 0
        for element in crumbCoords:
            crumb = StaticItems.Breadcrumb(element)
            crumbs.append(crumb)

        crumbSpots = pygame.sprite.Group (crumbs)
        return crumbSpots


    def potionCoords (self):
        potionCoords = []
        potions = []
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == '*':
                    potion = ((gridX * countx - (gridX/2) + startx, gridY * county - (gridY/2) + starty))
                    potionCoords.append(potion)
            county +=1
            countx = 0
        for element in potionCoords:
            potion = StaticItems.Potion(element)
            potions.append(potion)

        potionSpots = pygame.sprite.Group (potions)
        return potionSpots




    def dragonSprites(self):
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        dragoncoords = []
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == '$':
                    dragoncoord = ((gridX * countx + (gridX/2) + startx, gridY * county - (gridY/2) +starty))
                    dragoncoords.append(dragoncoord)
            county +=1
            countx = 0
        return dragoncoords




    def treasureStart (self):
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == '+':
                   tstart= ((gridX * countx + (gridX/2) + startx, gridY * county - (gridY/2) +starty))
            county +=1
            countx =0
        return tstart

    def princessStart (self):
        mazeLayout = self.maze
        gridX = self.gridX
        gridY = self.gridY
        startx = self.startx
        starty = self.starty
        countx = 0
        county = 1
        for row in mazeLayout:
            for element in row:
                countx +=1
                if element == 'Q':
                    princessPos = ((gridX * countx + (gridX/2) + startx, gridY * county - (gridY/2) +starty))
            county +=1
            countx = 0
        return princessPos
