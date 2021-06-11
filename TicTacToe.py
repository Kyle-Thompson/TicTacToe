#Things to fix: Grid is upside down, code is repeated for X and O, sometimes it prints multiple win
#statements

selections = []

playerX = [] #
playerO = [] #'O' the letter

winCondition = 3 #number of tiles to match in a row

rows = 3
columns = 3

gridSize = rows*columns

for index in range(gridSize):
    selections.append (" ")

for index in range(gridSize):
    playerX.append (-1)

for index in range(gridSize):
    playerO.append (-1)

idx = 0

#Starting grid
incre = 0
print ("Welcome to Py Tac Toe! The grid will be numbered as follows:")
for i in range(rows):
    row = "|"
    for j in range(columns):
            row = row+str(j+incre+1)+"|"
    incre = incre + columns            
    print (row)

while idx < gridSize**2:
    gameOver = False

    

    userChoice = input("Pick a number: ")

    if userChoice.isdigit() == True:
        sel = int(userChoice)
        if sel < 1 or sel > len(selections):
            print("Please pick a number between 1 and "+str(rows*columns))
            continue

        if selections[sel-1] != " ":
            print("""Please don't try to cheat by writing over your opponent's
squares, you cheeky little wanker""")
            continue
    else:
        print ("Please input a number")
        continue

    if (idx%2 == 0):
        selections[sel-1] = "x"
        playerX[idx] = sel
    else:
        selections[sel-1] = "o"
        playerO[idx] = sel

    #Print the grid
    incre = 0
    for i in range(rows):
        row = "|"
        for j in range(columns):
            row = row+selections[j+incre]+"|"
        incre = incre + columns            
        print (row)

    #Win conditions

    #Win by row
    rowPos = 0
    for j in range(rows):
        rowOneX = []
        rowOneO = []

        for i in range(columns):
            for tile in range(len(playerX)):
                if i + rowPos + 1 == playerX[tile]:
                    rowOneX.append(playerX[tile])
                if i + rowPos + 1 == playerO[tile]:
                    rowOneO.append(playerO[tile])
                if len(rowOneX) == winCondition:
                    gameOver = True
                    print('X wins')
                    break
                if len(rowOneO) == winCondition:
                    gameOver = True
                    print('O wins')
                    break
        rowPos = rowPos + columns

    rowPos = 0

    #Win by column 
    colPos = 0
    for j in range(columns):
        colOneX = []
        colOneO = []
        numToCheckFor = j + 1
        for i in range(rows):
            for tile in range(len(playerX)):
                if  numToCheckFor == playerX[tile]:
                    colOneX.append(playerX[tile])
                if  numToCheckFor == playerO[tile]:
                    colOneO.append(playerO[tile])    
                if len(colOneX) == winCondition:
                    gameOver = True
                    print('X wins')
                    break
                if len(colOneO) == winCondition:
                    gameOver = True
                    print('O wins')
                    break                
            numToCheckFor = numToCheckFor + columns
    

    #Win by Forward Diagonal
    colPos = 0
    for j in range(columns):
        colOneX = []
        colOneO = []

        numToCheckFor = j + 1
        for i in range(rows):
            for tile in range(len(playerX)):
                if  numToCheckFor == playerX[tile]:
                    colOneX.append(playerX[tile])
                if  numToCheckFor == playerO[tile]:
                    colOneO.append(playerO[tile])
                if len(colOneX) == winCondition:
                    gameOver = True
                    print('X wins')
                    break
                if len(colOneO) == winCondition:
                    gameOver = True
                    print('O wins')
                    break
            numToCheckFor = numToCheckFor + columns + 1

    #Win by Backward Diagonal (1,5,3/2,4,6 etc wins because this funtionally ony checks for an
    # of 2) Floor division is key to sorting out a distinction of rows.
    colPos = 0
    for j in range(columns):
        colOneX = []
        colOneO = []

        numToCheckFor = j + 1
        for i in range(rows):
            for tile in range(len(playerX)):
                if len(colOneX) > 0:
                    if  numToCheckFor == playerX[tile] and playerX[tile]//(i+1) != colOneX[len(colOneX)-1]//(i+1):
                        colOneX.append(playerX[tile])
                    else:
                        continue
                else:
                    if  numToCheckFor == playerX[tile]:
                        colOneX.append(playerX[tile])
                       
                if len(colOneO) > 0:
                    if  numToCheckFor == playerO[tile] and playerO[tile]//(i+1) != colOneO[len(colOneO)-1]//(i+1):
                        colOneO.append(playerX[tile])
                    else:
                        continue
                else:
                    if  numToCheckFor == playerO[tile]:
                        colOneO.append(playerO[tile])
                if len(colOneX) == winCondition:
                    gameOver = True
                    print('X wins')
                    break
                if len(colOneO) == winCondition:
                    gameOver = True
                    print('O wins')
                    break
            numToCheckFor = numToCheckFor + columns - 1

    if gameOver == True:
        break
    
    idx = idx + 1 
