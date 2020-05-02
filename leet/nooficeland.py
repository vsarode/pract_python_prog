"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
visited_iceland = []


def traverse_iceland(icel, i, j, l):
    if icel[i][j]==0:
        return
    if icel[i-1][j]==1:
        return traverse_iceland(icel, i-1, j)
    if icel[i+1][j] ==  1:
        return 



def no_of_iceland(icel):
    iceland = 0
    for i in icel:
        for j in i:
            if j == 1 and (i, j) not in visited_iceland:
                traverse_iceland(i, j, len(icel))
                iceland += 1
    return iceland
