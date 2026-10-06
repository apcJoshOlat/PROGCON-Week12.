PSEUDOCODE: 
 
Function Main 
    Declare String box1 
    Declare String box2 
    Declare String box3 
    Declare String currentPlayer 
    Declare Boolean gameOver 
    Declare Integer choice 
    Declare Integer computerChoice 
 
    Assign box1 = " " 
    Assign box2 = " " 
    Assign box3 = " " 
    Assign gameOver = false 
    Declare Integer firstTurn 
 
    Assign firstTurn = Random(2) 
    Declare Boolean validMove 
 
    Assign validMove = false 
    If firstTurn = 0 
        Assign currentPlayer = "User" 
    Else 
        Assign currentPlayer = "Computer" 
    End 
    While gameOver = false 
        If currentPlayer = "User" 
            Assign validMove = false 
            While validMove = false 
                Output "Your turn. Choose a box (1-3): " 
                Input choice 
                If choice = 1 AND box1 = " " 
                    Assign box1 = "O" 
                    Assign validMove = true 
                Else 
                    If choice = 2 AND box2 = " " 
                        Assign box2 = "O" 
                        Assign validMove = true 
                    Else 
                        If choice = 3 AND box3 = " " 
                            Assign box3 = "O" 
                            Assign validMove = true 
                        Else 
                            Output "Invalid choice. Choose an empty box." 
                        End 
                    End 
                End 
            End 
        Else 
            Assign validMove = false 
            While validMove = false 
                Assign computerChoice = Random(3) + 1 
                If computerChoice = 1 AND box1 = " " 
                    Assign box1 = "X" 
                    Assign validMove = true 
                Else 
                    If computerChoice = 2 AND box2 = " " 
                        Assign box2 = "X" 
                        Assign validMove = true 
                    Else 
                        If computerChoice = 3 AND box3 = " " 
                            Assign box3 = "X" 
                            Assign validMove = true 
                        End 
                    End 
                End 
            End 
        End 
        If box1 = box2 AND box2 = box3 AND box1 != " " 
            If box1 = "O" 
                Output "User wins!" 
                Assign gameOver = true 
            Else 
                Output "Computer wins!" 
                Assign gameOver = true 
            End 
        Else 
            If box1 != " " AND box2 != " " AND box3 != " " 
                Output "It's a draw!" 
                Assign gameOver = true 
            Else 
                If currentPlayer = "User" 
                    Assign currentPlayer = "Computer" 
                Else 
                    Assign currentPlayer = "User" 
                End 
            End 
        End 
    End 
End 
