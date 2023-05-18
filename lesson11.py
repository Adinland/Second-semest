
print("Задание 1")
def my_func(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

a  = int(input())
f = my_func(a)
print(f"Факториал = {f}")
my_list = []
for i in range(f, 0, -1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    my_list.append(fact)
print(my_list)
