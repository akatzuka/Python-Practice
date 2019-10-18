class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

                #Top: matrix[y][x]
                #Bottom: matrix[N-1-x][N-1-y]
                #Left: matrix[N-1-y][x]
                #Right: matrix[y][N-1-x]

                # store current cell
                # move values from right to top
                # move values from bottom to right
                # move values from left to bottom
                # assign temp to left

                temp = matrix[x][y]
                matrix[x][y] = matrix[y][N-1-x]
                matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
                matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
                matrix[N-1-y][x] = temp
