class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #matrix = numpy.rot90(matrix, 1)
        N = len(matrix)

        #all squares
        for x in range(0,int(N/2)):
            #all elements in current square as a group of 4
            for y in range(x, N-x-1):

                #Top: matrix[y][x]
                #Bottom: matrix[N-1-x][N-1-y]
                #Left: matrix[N-1-y][x]
                #Right: matrix[y][N-1-x]

                # store current cell
                # move values from left to top
                # move values from bottom to left
                # move values from right to bottom
                # assign temp to right

                temp = matrix[x][y]
                matrix[x][y] = matrix[N-1-y][x]
                matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
                matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
                matrix[y][N-1-x] = temp

                
