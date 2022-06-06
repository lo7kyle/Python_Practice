"""
This file will use BFS to find how long it will take to find the rotting oranges adjacent to rotten oranges in a 2D Grid
If given a grid of 1 being fresh 2 being rotten and 0 being no oranges we need to return the time it takes for the entire batch of oranges to be rotten. Each minute that passes by, the oranges adjacent to the rotten one 
will be rotten
ex: 
Input:
2 1 1 0
1 1 0 2
2 1 0 0

Output:
2
Approach: Object oriented programming to practice OOP
"""

from collections import deque as queue

class rottingOranges:

    # Instance Attribute
    def __init__(self, row, col, grid):
        self.ROW = row
        self.COL = col
        self.grid = grid

    # Check to see if the adjacent cells are Fresh or not
    def isFresh(self,i, j, rotten):
        # if the adjacent lies outside the grid, return false
        if(i < 0 or j < 0 or i >= self.ROW or j >= self.COL):
            return False
        # if the orange is already rotten, return false
        if (rotten[i][j]):
            return False
        # if it is not rotten or outside boundaries, it is a fresh orange
        return True

    # getTime of when all the oranges will be rotten
    def getTime(self):
        # Initialize Queue
        q = queue()
        minute = 0
        # Initialize rotten grid to keep count of which oranges are rotten
        rotten = [[False for j in range(self.COL)] for i in range(self.ROW)]
           
        # Direction vectors to check adjacency cells
        dRow = [-1, 0, 1, 0]
        dCol = [0, 1, 0, -1]

        # Initially Mark grid for rotten Oranges 
        for i in range(self.ROW):
            for j in range(self.COL):
                if rotten[i][j] == False and self.grid[i][j] == 2:
                    rotten[i][j] = True
                    q.append((i, j))
        while(len(q)):
            cell = q.popleft()
            current_queue = len(q)
            x = cell[0]
            y = cell[1]

            # Go to the adjacent cells of current cell (x,y)
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if (self.isFresh(adjx, adjy, rotten) and self.grid[adjx][adjy] != 0):
                    q.append((adjx, adjy))
                    rotten[adjx][adjy] = True
                    grid[adjx][adjy] = 2
                
            new_queue = len(q)
            if(current_queue != new_queue):
                minute += 1
                self.printGrid()
                print('\n')

        print(f'It will Take {minute} minutes until all of the oranges become rotten!')

    # Prints the grid for visualization of BFS
    def printGrid(self):
        for s in self.grid:
            print(*s)

# Main function
if __name__ == '__main__':
    grid = [[2,1,1,2,1,0],[1,1,0,1,1,1],[0,1,1,0,2,0],[2,1,1,2,1,0],[1,1,0,1,1,1],[0,1,1,0,2,0]] 
    # Get max row/col length
    row = len(grid)
    col = len(grid[0])

    g = rottingOranges(row, col, grid)

    # Pass instance into getTime method
    print(f'Original Input: \n***********')
    g.printGrid()
    print('***********')
    print('\n')
    g.getTime()