"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

# island = 1 surrounded by 0, adjacent = 0
# outside bounds = 0

# A function to check if a given cell
# (row, col) can be included in DFS
def isSafe(grid, i, j, maxRow, maxCol, visited):
    # row number is in range, column number
    # is in range and value is 1
    # and not yet visited
    return (i >= 0 and i < maxRow and
            j >= 0 and j < maxCol and
            not visited[i][j] and grid[i][j])
  
# Use DFS to check neighbors
def DFS(grid, visited, i, j, maxRow, maxCol):
    
    # Check for adjacent cells
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]
    # Mark current cell as visited
    visited[i][j] = True
    
    
    # will check the adjacent cells using dRow/dCol
    for k in range(4):
        adjx = i + dRow[k]
        adjy = j + dCol[k]
        if(isSafe(grid, adjx, adjy, maxRow, maxCol, visited) and grid[adjx][adjy] == 1):
            DFS(grid, visited, adjx, adjy, maxRow, maxCol)
                

    
    
def printIsland(grid):
    for s in grid:
        print(*s)

def findNumberOfIsland(grid):  
    maxRow = len(grid)
    maxCol = len(grid[0])
    
    # Separate list to track what has been visited
    visited = [[False for j in range(maxCol)] for i in range(maxRow)]
    islands = 0
    
    for i in range(maxRow):
        for j in range(maxCol):
            if (visited[i][j] == False and grid[i][j] == 1):
                DFS(grid, visited, i, j, maxRow, maxCol)
                islands += 1

    print(f'There are {islands} islands')

if __name__=='__main__':
    
    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
    
#     grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#     ]
    
    
    #print island for visualization
    printIsland(grid)

    # call number of island function with (0,0) as our starting point
    findNumberOfIsland(grid)
  
