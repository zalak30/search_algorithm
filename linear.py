from datetime import datetime

start = datetime.now()
lst = [1, 4, 8, 9, 9, 54, 87, 91, 9]


def linear_search(n, nums):
    for index, num in enumerate(nums):
        if num == n:
            print("index of {} is {}".format(n, index))
        elif num % 10 == 0:
            print("{} is completed".format(num))


linear_search(9, lst)
end = datetime.now()
print(end-start)
