import random
random.seed()   #Prepare random number generator

box1 = " "
box2 = " "
box3 = " "
gameOver = False
firstTurn = int(random.random() * 2)
validMove = False
if firstTurn == 0:
    currentPlayer = "User"
else:
    currentPlayer = "Computer"
while gameOver == False:
    if currentPlayer == "User":
        validMove = False
        while validMove == False:
            print("Your turn. Choose a box (1-3): ")
            choice = int(input())
            if choice == 1 and box1 == " ":
                box1 = "O"
                validMove = True
            else:
                if choice == 2 and box2 == " ":
                    box2 = "O"
                    validMove = True
                else:
                    if choice == 3 and box3 == " ":
                        box3 = "O"
                        validMove = True
                    else:
                        print("Invalid choice. Choose an empty box.")
    else:
        validMove = False
        while validMove == False:
            computerChoice = int(random.random() * 3) + 1
            if computerChoice == 1 and box1 == " ":
                box1 = "X"
                validMove = True
            else:
                if computerChoice == 2 and box2 == " ":
                    box2 = "X"
                    validMove = True
                else:
                    if computerChoice == 3 and box3 == " ":
                        box3 = "X"
                        validMove = True
    if box1 == box2 and box2 == box3 and box1 != " ":
        if box1 == "O":
            print("User wins!")
            gameOver = True
        else:
            print("Computer wins!")
            gameOver = True
    else:
        if box1 != " " and box2 != " " and box3 != " ":
            print("It's a draw!")
            gameOver = True
        else:
            if currentPlayer == "User":
                currentPlayer = "Computer"
            else:
                currentPlayer = "User"
