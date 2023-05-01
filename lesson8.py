print("\tЗадание 1\nВведите размер, затем содержимое списка")
len = int(input())
arr = []
for i in range(len):
    arr.append(int(input()))
arr.reverse()
print(arr)

print("\tЗадание 2\nВведите размер, затем содержимое списка")
len = int(input())
arr = []
for i in range(len):
    arr.append(int(input()))
arr = arr[-1:] + arr[:-1]
print(arr)


print("\tЗадание 3\nВведите грузоподьёмность лодки, количество людей, затем вес каждого")
b_weight = int(input())
amount_people = int(input())
p_weight = []
for i in range(amount_people):
    p_weight.append(int(input()))
"""
тестовые данные
b_weight = 120
amount_people = 5
p_weight = [50, 60, 65, 100, 50]
3 лодки
"""
all_weight = 0
amount_boat = 0
for i in p_weight:
    all_weight += i
if all_weight < b_weight:
    while amount_people > 0:
        amount_boat += 1
        amount_people -= 2
elif all_weight > b_weight:
    while all_weight > 0:
        amount_boat += 1
        all_weight -= b_weight
elif all_weight % b_weight == 0:
    while all_weight > 0:
        amount_boat += 1
        all_weight -= b_weight
print(f"Минимально необходимое количество лодок: {amount_boat}")
