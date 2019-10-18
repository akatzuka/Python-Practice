def searchInsert(self, nums: List[int], target: int) -> int:
    #Linear Search
        if not nums:
            return 0

        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)

    #Binary Search
    #    low, high = 0, len(nums)
    #
    #    while low < high:
    #        mid = (low + high) // 2
    #        if target > nums[mid]:
    #            low = mid + 1
    #
    #        else:
    #            high = mid
    #
    #    return low
