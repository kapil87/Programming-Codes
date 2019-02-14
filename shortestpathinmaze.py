def issafe(mat, visited, x, y):
    """If position x,y is 0 or its already visited return False"""
    print (x,y)
    if mat[x][y] == 0 or visited[x][y] ==1:
        return False
    return True

def isvalid(x, y):
    """Check If x,y is valid co-ordinates"""
    return (x<M and y <N and x>= 0 and y >=0)

def findshortedtpath(mat, visited, i, j, x, y, min_dist, dist):
    print (i,j, min_dist, dist)
    print (visited)
    #If destination is found
    if i == x and j == y:
        print (min_dist, dist)
        min_dist = min(dist, min_dist)
    #set i, j as visited
    visited[i][j] = 1

    #Go to bottom cell
    if (isvalid(i+1, j) and issafe(mat, visited, i+1, j)):
        print ('goint to bottom, [%s][%s]'%(i+1, j))
        min_dist = findshortedtpath(mat, visited, i+1, j, x, y, min_dist, dist+1)

    #Go to right cell
    if (isvalid(i, j+1) and issafe(mat, visited, i, j+1)):
        print('goint to right, [%s][%s]' % (i, j+1))
        min_dist = findshortedtpath(mat, visited, i, j+1, x, y, min_dist, dist+1)

    #Go to top cell
    if (isvalid(i-1, j) and issafe(mat, visited, i-1, j)):
        print('goint to top, [%s][%s]' % (i-1, j))
        min_dist = findshortedtpath(mat, visited, i-1, j, x, y, min_dist, dist+1)

    #Go to left cell
    if (isvalid(i, j-1) and issafe(mat, visited, i, j-1)):
        print('goint to left, [%s][%s]' % (i, j-1))
        min_dist = findshortedtpath(mat, visited, i, j-1, x, y, min_dist, dist+1)

    #backtrack, remove i, j from visited matrix
    print ('Backtracking')
    visited[i][j] = 0
    return min_dist

if __name__== '__main__':
    M, N = 10, 10
    mat =[
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    ]
    visited = [[0 for i in range(M)] for i in range(N)]
    print (visited)
    #global min_dist
    min_dist = 666531
    distance = findshortedtpath(mat, visited, 0,0, 7,5, min_dist, 0)
    print (distance)
