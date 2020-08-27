from datetime import datetime
nums = range(10000000)

start = datetime.now()

for num in nums:
    if (num % 10000) == 0:
        print("{} is completed".format(num))


end = datetime.now()
print(end-start)
