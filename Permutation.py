class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #DFS Solution
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result):
        if not nums:
            result.append(path)

            #return/backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], result)


    # def permutation(self, nums: List[int]) ->List[List[int]]:
    #     #if list is empty, then no permutations
    #     if len(nums) == 0:
    #         return []
    #
    #     #if only one element, then only one permutation is possible
    #     if len(nums) == 1:
    #         return [nums]
    #
    #     #if more that one element, find all permutations
    #     perm_list = [] #empty list for storing permutations
    #
    #     for i in range(len(nums)):
    #         #extract nums[i]
    #         #remain is the remaining elements in the list
    #
    #         x = nums[i]
    #         remain = nums[:i] + nums[i+1:]
    #
    #         #generate remaining permutations
    #         for j in permutation(remain):
    #             perm_list.append([x] + j)
    #
    #     return perm_list
    #
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     nums = permutation(nums)
