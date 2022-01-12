import sys
#Tic-tac-Toe starter code

def reset_board():
    board = []
    for i in range(1,10):
        board.append(str(i))
    return(list(board))


#Takes in current game board and prints player positions on board
def print_board(board):
    #since the code above can be any length - we need to set the print to accomodate it
    breakrow = 3
    board_print = "\n "
    for b in range(0,len(board)):
        # for every time we hit breakrow, no vertical, and print the dash row
        #but no dash row at the end 
        if (b+1) % breakrow != 0:
            board_print += board[b]+ " | "
        elif (b+1) < len(board)-1:
            board_print += board[b]+"\n ---------\n "
        else:
            board_print += board[b]
    board_print += "\n"
    print(board_print)



#TODO:
#Create a function or multiple functions to check for a winner
def check_for_winner(board):
    pass
    """
    check_for_winner(board) determines if their is a draw or a winner 
    :param board: list with current game state and available positions
    :return: No return; prints game 
"""
    #TO-DO:
    #Check for diagonal winner
    ##Determine what else decides a winner
   
            
def keep_playing():
    """
    Asks user if they would like to continue game play
    :param None
    :ouput: resets game if user decides to play again and exits program otherwise. 
    """
    x = input("Would you like to play again? y or n? ").lower()
    if (x == "n"):
        print("Thank you for playing our game!")
        sys.exit("Thank you for playing our game!")
    else:
        current_board = []
        player_one = input('Would you like to be "X\'s" or "O\'s: '  ).upper()
        reset_board()

#return piece{String} - the player's piece, X or an O
#TODO
    #setup return
    #while loop so it keeps asking until player puts proper piece
def get_player_piece():
    piece = input('Would you like to be "X\'s" or "O\'s: '  ).upper()
    if(piece != "X" or piece != "O"):
        piece = input('Please learn to read. We need "X\'s" or "O\'s for this game. Do you want X\'s or O\'s? '  ).upper()
       
        # \ is the escape charater
    
"""
MAIN GAME LOOP
"""
#Game Loop
game_over = False
winner = -1
player_one = get_player_piece()
#input('Would you like to be "X\'s" or "O\'s: '  ).upper()
player_two = ""
if (player_one == "X"):
    player_two = "O"
else:
    player_two = "X"

current_board = reset_board()

while (not game_over):
    #TO-DO:
    #complete game loop below
    #make a plan using psuedo code. 
    print_board(current_board)

    #player what position player wants to play at
    #Print out new coard with player choice 
    #check if player1 wins
    pos = int(input("Player 1 what position on board do you want to play on board? "))
    
    current_board[pos-1] = player_one
    print_board(current_board)
    #player 2 position for play
    #print board 
    #check if player 2 wins
    pos = int(input("Player 2 what position on board do you want to play on board? "))
    current_board[pos-1] = player_two
    print_board(current_board)

    #keep_playing is called below in the starter code to allow us to see the game loop. Decide as a class if it is needed. 
    
    if (winner != -1):
        game_over = True
        keep_playing()
    


        









