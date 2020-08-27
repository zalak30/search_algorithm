from datetime import datetime
start = datetime.now()

lst = [1, 4, 8, 9, 9, 54, 87, 91, 9]


def binary_search(n, nums):
    nums.sort()
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high)//2
        item = nums[mid]
        if n == item:
            return mid
        elif n < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


binary_search(9, lst)
end = datetime.now()
print(end-start)
