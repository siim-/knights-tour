##Knights tour
##School assignment, December 2011
##Revised: October 2012

import time

#Self-explanatory constants
START_TIME = time.time() 
BOARD_SIZE = 5 
BOARD = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

#Print the board with pretty formatting
def pretty_print():
    i = BOARD_SIZE
    print("Solution:")
    print("{0:2}".format(''),end='')
    for j in range(10,10+BOARD_SIZE):
        print("{0:2}|".format(chr(j+55)),end='')
    print('')
    for rows in BOARD:
        print("{0:1}|".format(i),end='')
        for elements in rows:
            print("{0:2}|".format(elements),end='')
        print('')
        i=i-1
    print('')

#Return a list of valid moves
#Params: pos   - The current position of the knight piece [0=y,1=x]
def valid_moves(pos):
    moves = []
    #Check all 8 possible moves
    #Move 1
    if ((pos[0]-2>-1) and (pos[1]-1>-1)):
        if (BOARD[pos[0]-2][pos[1]-1] == 0):
            moves.append([pos[0]-2,pos[1]-1])
    #Move 2
    if ((pos[0]-2>-1) and (pos[1]+1<BOARD_SIZE)):
        if (BOARD[pos[0]-2][pos[1]+1] == 0):
            moves.append([pos[0]-2,pos[1]+1])
    #Move 3
    if ((pos[0]+2<BOARD_SIZE) and (pos[1]-1>-1)):
        if (BOARD[pos[0]+2][pos[1]-1] == 0):
            moves.append([pos[0]+2,pos[1]-1])
    #Move 4
    if ((pos[0]+2<BOARD_SIZE) and (pos[1]+1<BOARD_SIZE)):
        if (BOARD[pos[0]+2][pos[1]+1] == 0):
            moves.append([pos[0]+2,pos[1]+1])
    #Move 5
    if ((pos[0]-1>-1) and (pos[1]+2<BOARD_SIZE)):
        if (BOARD[pos[0]-1][pos[1]+2] == 0):
            moves.append([pos[0]-1,pos[1]+2])
    #Move 6
    if ((pos[0]-1>-1) and (pos[1]-2>-1)):
        if (BOARD[pos[0]-1][pos[1]-2] == 0):
            moves.append([pos[0]-1,pos[1]-2])
    #Move 7
    if ((pos[0]+1<BOARD_SIZE) and (pos[1]-2>-1)):
        if (BOARD[pos[0]+1][pos[1]-2] == 0):
            moves.append([pos[0]+1,pos[1]-2])
    #Move 8
    if ((pos[0]+1<BOARD_SIZE) and (pos[1]+2<BOARD_SIZE)):
        if (BOARD[pos[0]+1][pos[1]+2] == 0):
            moves.append([pos[0]+1,pos[1]+2])
        
    return moves
    
#Make a move
#Params: number - The number of the current move
#        to     - The square to move to [0=y,1=x]
def move(number,to):
    BOARD[to[0]][to[1]],return_value = number,False
    
    for row in BOARD:
        if(0 not in row):
            return_value = True
        else:
            return_value = False
            break

    for moves in valid_moves(to):
        if(move(number+1,moves)):
            return_value = True
            break
            
    if return_value:
        print("Solved {0}x{0} board in {1} seconds".format(BOARD_SIZE,time.time()-START_TIME))
        pretty_print()
        exit()
        
    if not return_value:
        BOARD[to[0]][to[1]] = 0
       
    return return_value

#Perform the Knight's tour
#Params: start - List containing the starting position [0=y,1=x]
def tour(start):
    BOARD[start[0]][start[1]],return_value = 1, False
    for moves in valid_moves(start):
         if(move(2,moves)):
             return_value = True
             break 
    return return_value
    
if __name__ == '__main__':
    start_time = time.time()
    start = [0,0] #Edit at your leisure
    print("Solving a {0}x{0} board...".format(BOARD_SIZE))
    print("Starting from {0}...".format(start))
    tour(start)