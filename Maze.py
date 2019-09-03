import pygame
import random
pygame.init()

screenSize = screenWidth, screenHeight = 500, 500
gridSize = gridWidth, gridHeight = 25, 25
boxSize = boxWidth, boxHeight = 23, 23
window = pygame.display.set_mode((screenSize))
pygame.display.set_caption("Maze")
allBoxes = []

# Create maze background
window.fill(0)
for i in range(1,11):
    for j in range (1,11):
        newRectPos = rectLeft, rectTop = 25*(i-1), 25*(j-1)
        allBoxes.append((newRectPos))
        newRect = pygame.Rect(rectLeft, rectTop, boxWidth, boxHeight)
        if newRectPos == (0,0) or newRectPos == (225,225): pygame.draw.rect(window, (225,0,225), newRect)
        else: pygame.draw.rect(window, (250,250,250), newRect)

def RemoveTopWall(xPos, yPos):
    newRect = pygame.Rect(xPos, yPos-2, boxWidth, 2)
    pygame.draw.rect(window, (250,250,250), newRect)
    pygame.display.update()

def RemoveBottomWall(xPos, yPos):
    newRect = pygame.Rect(xPos, yPos+boxHeight, boxWidth, 2)
    pygame.draw.rect(window, (250,250,250), newRect)
    pygame.display.update()

def RemoveRightWall(xPos, yPos): 
    newRect = pygame.Rect(xPos+boxWidth, yPos, 2, boxHeight)
    pygame.draw.rect(window, (250,250,250), newRect)
    pygame.display.update()

def RemoveLeftWall(xPos, yPos): 
    newRect = pygame.Rect(xPos-2, yPos, 2, boxHeight)
    pygame.draw.rect(window, (250,250,250), newRect)
    pygame.display.update()

def CreateMaze():
    currentBox = (0,0)
    currentXPos = currentBox[0]
    currentYPos = currentBox[1]
    boxesToCheck = []
    visitedBoxes = []
    visitedBoxes.append(currentBox)
    boxesToCheck.append(currentBox)
    while len(boxesToCheck) > 0:
        adjacentBoxes = []
        # Check cell above
        if (currentXPos,currentYPos-gridHeight) in allBoxes and (currentXPos,currentYPos-gridHeight) not in visitedBoxes:
            adjacentBoxes.append((currentXPos, currentYPos-gridHeight))
        # Check cell below
        if (currentXPos,currentYPos+gridHeight) in allBoxes and (currentXPos,currentYPos+gridHeight) not in visitedBoxes:
            adjacentBoxes.append((currentXPos,currentYPos+gridHeight))
        # Check cell to the right
        if (currentXPos+gridWidth,currentYPos) in allBoxes and (currentXPos+gridWidth,currentYPos) not in visitedBoxes:
            adjacentBoxes.append((currentXPos+gridWidth,currentYPos))
        # Check cell to the left
        if (currentXPos-gridWidth,currentYPos) in allBoxes and (currentXPos-gridWidth,currentYPos) not in visitedBoxes:
            adjacentBoxes.append((currentXPos-gridWidth,currentYPos))

        if len(adjacentBoxes) <= 0:
            currentBox = boxesToCheck.pop()
            currentXPos = currentBox[0]
            currentYPos = currentBox[1]
        else:
            num = random.randint(0,len(adjacentBoxes)-1)
            randAdjBox = adjacentBoxes[num]
            currentBox = (currentXPos,currentYPos)
            if randAdjBox == (currentXPos,currentYPos-gridHeight): # top box
                RemoveTopWall(currentXPos,currentYPos)
                currentYPos -= 25
            elif randAdjBox == (currentXPos,currentYPos+gridHeight): # bottom box
                RemoveBottomWall(currentXPos,currentYPos)
                currentYPos += 25
            elif randAdjBox == (currentXPos+gridWidth,currentYPos): # right box
                RemoveRightWall(currentXPos,currentYPos)
                currentXPos += 25
            elif randAdjBox == (currentXPos+-gridWidth,currentYPos): # left box
                RemoveLeftWall(currentXPos,currentYPos)
                currentXPos -= 25

            visitedBoxes.append(randAdjBox)
            boxesToCheck.append(randAdjBox)

  
CreateMaze()

            
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

