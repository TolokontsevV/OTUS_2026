def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count


nums = [10, 15, 20]
Result = calculate_average(nums)
print("The average is:", Result)