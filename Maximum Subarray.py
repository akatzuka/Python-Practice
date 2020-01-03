class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:   #if array is empty, return 0
            return 0

        cSum = maxSum = nums[0]     #set current sum and max sum equal to first element of nums
        for num in nums[1:]:        #for every element in nums, starting with the second element
            cSum = max(num, cSum + num)     #set current sum to the max of the current element and the current element + current sum
            maxSum = max(maxSum, cSum)      #set max sum to the max of max sum and the current sum

        return maxSum               #return max sum
