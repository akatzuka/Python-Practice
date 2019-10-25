class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #In-place, O(1) memory:
        for i in range(len(A)):
            A[i] *= A[i]
        A.sort()
        return A

        #New array, not in-place, O(n) auxiliary space
        return sorted([v**2 for v in A])

        #New array, not in place, O(1) aux space
        return_array = [v**2 for v in A]
        return_array.sort() #In-place
        return return_array

        #Deque Method, O(n) time complexity, O(n) aux space
        number_deque = collections.deque(A)
        reverse_squares = []
        while number_deque:
            left_square = number_deque[0] ** 2
            right_square = number_deque[-1] ** 2
            if left_square > right_square:
                reverse_squares.append(left_square)
                number_deque.popleft()
            else:
                reverse_squares.append(right_square)
                number_deque.pop()
        return reverse_squares[::-1]

        #Create deque based off of list A
        #Create list for holding reverse sorted squares
        #While loop for as long as number_deque has elements:
        #left_square is equal to the square of the current deque element
        #right_square is equal to the square of the previous deque element
        #If comparison: If left_square is greater than right_square:
            #Append left_square to the sorted squares list
            #popleft number_deque (removes and returns element from the left side of the deque)
        #Else:
            #Append right_square to the sorted squares list
            #pop number_deque (removes and returns element from the right side of the deque)
        #Return reverse of reverse_squares list ([::-1] is a slice that is all list elements in reverse order)
