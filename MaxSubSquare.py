# Python3 code for Maximum size 
# square sub-matrix with all 1s 
  
import numpy as np

def printMaxSubSquare(M): 
    #R = len(M) # no. of rows in M[][] 
    #C = len(M[0]) # no. of columns in M[][] 
    Row, Col = M.shape 
    
    #S = [[0 for k in range(Col)] for l in range(Row)]
    S = np.zeros((Row, Col), dtype=int)
    # here we have set the first row and column of S[][] 
  
    # Construct other entries 
    for i in range(1, Row): 
        for j in range(1, Col): 
            if (M[i][j] == 1): 
                S[i][j] = min(S[i][j-1], S[i-1][j], 
                            S[i-1][j-1]) + 1
            else: 
                S[i][j] = 0
      
    # Find the maximum entry and 
    # indices of maximum entry in S[][]
    # find using loops
    #  max_of_s = S[0][0] 
    #  max_i = 0
    #  max_j = 0
    #  for i in range(Row): 
    #      for j in range(Col): 
    #          if (max_of_s < S[i][j]): 
    #              max_of_s = S[i][j] 
    #              max_i = i 
    #              max_j = j 

    # find using numpy functions
    # amax finds max of array/matrix
    # argmax finds flattened indicies of largest element
    # unravel_index un-flattens the result of argmax
    max_of_s = np.amax(S)
    max_i, max_j = np.unravel_index(np.argmax(S), shape = (Row, Col))
    
    #Printing max sub-matrix:
    #Looping through and printing:
    
    #print("Maximum size sub-matrix is: ") 
    #for i in range(max_i, max_i - max_of_s, -1): 
    #    for j in range(max_j, max_j - max_of_s, -1): 
    #        print (M[i][j], end = " ") 
    #    print("") 
    
    #OR
    #Generate matrix of ones of max size, and print:
    X = np.ones(shape=((max_i -  (max_i - max_of_s)),(max_j -  (max_j - max_of_s))), dtype=int)
    print(X)  
    
    
    #Printing dimensions of sub-matrix:
    print("Dimensions: ")
    print(X.shape)
    print("")
  
# Driver Program 
m = np.array([[0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0]] ) 
    
n = np.array([[1, 1, 0, 0, 1, 1], 
    [1, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 0], 
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0]] )
    
printMaxSubSquare(m) 
printMaxSubSquare(n)
