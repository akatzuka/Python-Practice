class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #set index counter to 0
        #loop will run from 0 until length of nums array - 1 (as we will be checking the next element always)
        #compare element at current index with the next element
        #if numbers are the same, delete current element, and decrement counter back one
        #if numbers are not the same, continue on
        #increment current_index and continue loop

        current_index = 0

        while current_index < len(nums) - 1:
            if nums[current_index] == nums[current_index+1]:
                del nums[current_index]
                current_index -= 1
            current_index += 1

        return len(nums)    #return the length of nums array
