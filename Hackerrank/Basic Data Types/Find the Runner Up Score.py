#!/usr/bin/python
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    largest = max(nums)

    while max(nums) == largest:
        nums.remove(max(nums))

    print(max(nums))

    #print(sorted(set(nums))[-2])
    #Alternative solution using sets
