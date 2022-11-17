N = int(input("Enter no of queens = "))

board = [[0]*N for _ in range(N)]


# def print_board():
#     for i in board:
#         print(i)
   
# print_board() 

def is_under_attack(i,j):
    # Check Same row or column
    for k in range(0, N):
        if((board[i][k]==1) or (board[k][j]==1)):
            return True
    
    # Check Diagonals
    for row in range(0, N):
        for col in range(0,N):
            if((row+col == i+j) or (row-col == i-j)):
                if(board[row][col] == 1):
                    return True
    
    return False # not in under attack   

def N_queen(n):
    if(n==0):
        return True # queen placed
    
    for i in range(0, N):
        for j in range(0, N):
            if(not(is_under_attack(i,j)) and board[i][j]!=1):
                board[i][j] = 1
                # place remaining queen
                if N_queen(n-1) == True:
                    return True
                # backtrack
                board[i][j] = 0
    
    return False # queen placed in wrong position
                 


N_queen(N)
for i in board:
    print(i)
# print_board()