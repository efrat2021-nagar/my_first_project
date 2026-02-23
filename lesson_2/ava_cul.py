from itertools import count

summery = 0
count = 0
for i in range(1,10):
   summery = summery + i
   count = count + 1

average = summery / count

nums= [23,45,234,565,67]
summery_list = 0
for num in nums:
    summery_list = summery_list + num
amount = len(nums)
avg_list = summery_list/amount
print (avg_list)