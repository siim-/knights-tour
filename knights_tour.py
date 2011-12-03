##Knight's tour
##Written by me in December 2011 as a school assignment

##This implementation of knight's tour can either run fast or slow. Testing shows that execution time can be variable.
##Worst case scenario might be that it takes hours.
##The following times were achieved on a 2x3.1Ghz AMD processor with 2GB of RAM.Running 32-bit python 3.2.2.
##Times:
##Solving a 5x5 board starting from [0,0] - ~0.4 seconds
##Solving a 6x6 board starting from [0,0] - ~90 seconds
##Solving a 7x7 board starting from [0,0] - ~5.6 seconds
##Solving a 8x8 board starting from [0,0] - Don't know, I am not a patient man.

import time

START_TIME = time.time() #Used for timing the program's execution
BOARD_SIZE = 5 #NB! Execution time grows with the board's size
DEBUG = False #Setting this to True makes the program's output more verbose but slows execution considerably. Use with smaller board sizes

#Print the board with pretty formatting
#Params: board - List containing the board to print
def pretty_print(board):
    i = BOARD_SIZE
    print("Solution:")
    print('')
    print("{0:2}".format(''),end='')
    for j in range(10,10+BOARD_SIZE):
        print("{0:2}|".format(chr(j+55)),end='')
    print('')
    for rows in board:
        print("{0:1}|".format(i),end='')
        for elements in rows:
            print("{0:2}|".format(elements),end='')
        print('')
        i=i-1
    print('')
    
#Dump the board
#Params: board - List containing the board to print
def dump_board(board):
    print('')
    for rows in board:
        print(rows)

#Return a list of valid moves
#Params: board - List containing current board
#        pos   - The current position of the knight piece [0=y,1=x]
def valid_moves(board,pos):
    moves = []
    #Check all 8 possible moves
    #Move 1
    if ((pos[0]-2>-1) and (pos[1]-1>-1)):
        if (board[pos[0]-2][pos[1]-1] == 0):
            moves.append([pos[0]-2,pos[1]-1])
    #Move 2
    if ((pos[0]-2>-1) and (pos[1]+1<BOARD_SIZE)):
        if (board[pos[0]-2][pos[1]+1] == 0):
            moves.append([pos[0]-2,pos[1]+1])
    #Move 3
    if ((pos[0]+2<BOARD_SIZE) and (pos[1]-1>-1)):
        if (board[pos[0]+2][pos[1]-1] == 0):
            moves.append([pos[0]+2,pos[1]-1])
    #Move 4
    if ((pos[0]+2<BOARD_SIZE) and (pos[1]+1<BOARD_SIZE)):
        if (board[pos[0]+2][pos[1]+1] == 0):
            moves.append([pos[0]+2,pos[1]+1])
    #Move 5
    if ((pos[0]-1>-1) and (pos[1]+2<BOARD_SIZE)):
        if (board[pos[0]-1][pos[1]+2] == 0):
            moves.append([pos[0]-1,pos[1]+2])
    #Move 6
    if ((pos[0]-1>-1) and (pos[1]-2>-1)):
        if (board[pos[0]-1][pos[1]-2] == 0):
            moves.append([pos[0]-1,pos[1]-2])
    #Move 7
    if ((pos[0]+1<BOARD_SIZE) and (pos[1]-2>-1)):
        if (board[pos[0]+1][pos[1]-2] == 0):
            moves.append([pos[0]+1,pos[1]-2])
    #Move 8
    if ((pos[0]+1<BOARD_SIZE) and (pos[1]+2<BOARD_SIZE)):
        if (board[pos[0]+1][pos[1]+2] == 0):
            moves.append([pos[0]+1,pos[1]+2])
        
    return moves
    
#Make a move
#Params: board  - List containing the current board
#        number - The number of the current move
#        to     - The square to move to [0=y,1=x]
def move(board,number,to):
    board[to[0]][to[1]] = number
    return_value = False
    for row in board:
        if(0 not in row):
            return_value = True
        else:
            return_value = False
            break
            
    if(DEBUG):
         print("Made move to {0}".format(to))
         dump_board(board)
   
    for moves in valid_moves(board,to):
        if(move(board,number+1,moves)):
            return_value = True
            break
            
    if return_value:
        pretty_print(board)
        print("Solved {0}x{0} board in {1} seconds".format(BOARD_SIZE,time.time()-START_TIME))
        exit()
        
    if not return_value:
        board[to[0]][to[1]] = 0
       
    return return_value

#Perform the Knight's tour
#Params: board - List containing the generated board
#        start - List containing the starting position [0=y,1=x]
def tour(board,start):
    board[start[0]][start[1]] = 1
    return_value = False
    if(DEBUG):
        print("Made move to {0}".format(start))
        dump_board(board)
        
    for moves in valid_moves(board,start):
         if(move(board,2,moves)):
             return_value = True
             break 
    return return_value
    
#The main entry point for the program
#Params: None
def main():
    start_time = time.time()
    board = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    start = [0,0] #Edit at your leisure
    print("Solving a {0}x{0} board...".format(BOARD_SIZE))
    print("Starting from {0}...".format(start))
    if DEBUG:
        print("Generated board...")
        dump_board(board)
    
    tour(board,start)
    
main()