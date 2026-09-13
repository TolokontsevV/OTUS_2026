def calculate_average(nums):
    total = sum(nums)
    count = len(nums)  # правка numbers на nums
    average = total / count
    return average  # добавлена строка return. Добавлена двойная пустая строка


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)  # правка Print на print, пустая строка