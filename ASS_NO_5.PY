# Design 8-Queens matrix having first Queen placed. Use backtracking to place remaining
# Queens to generate the final 8-queen’s matrix.

N = int(input("Enter the number of queens = ")) # 8 queen 

# Create NxN Size matrix
board = [[0]*N for _ in range(N)]


def is_attack(i, j):
    # Checking if there is a queen in row or column
    for k in range(0,N):
        if(board[i][k]==1 or board[k][j]==1):
            return True

    # Check Diagonals
    for row in range(0,N):
        for col in range(0,N):
            if((row+col==i+j) or (row-col==i-j)):
                if(board[row][col] == 1):
                    return True

    return False
        

def N_queen(n):
    if(n==0): # all queen are placed or n==0
        return True
    
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not queen will not be placed if the place is being attacked or already occupied'''
            if(not(is_attack(i,j)) and board[i][j]!=1 ):
                board[i][j] = 1
                # Place next queen recursively & check whether this combination is valid or not
                if N_queen(n-1) == True:
                    return True
                board[i][j] = 0
                
    return False 


N_queen(N)

for i in board:
    print(i)
