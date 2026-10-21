def median(nums):
    nums = sorted(nums)  # сортируем список
    n = len(nums)
    mid = n // 2  # индекс середины

    if n % 2 == 1:  # нечётное количество
        return nums[mid]
    else:  # чётное количество
        return (nums[mid - 1] + nums[mid]) / 2

# Запрашиваем количество чисел
n = int(input("Сколько чисел? "))

# Запрашиваем сами числа через пробел
print(f"Введите {n} чисел через пробел: ")
data = list(map(int, input().split()))

# Проверка на всякий случай, если ввели меньше чисел, чем указали
if len(data) != n:
    print("Ошибка: количество введенных чисел не совпадает с заявленным!")
else:
    print("Медиана:", median(data))