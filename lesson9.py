print("\tЗадание 1\nВведите количество элементов, затем сами элементы")
ln = int(input())
a = set()
for i in range(ln):
    num = int(input())
    a.add(num)
print(f"Уникальных чисел в списке: {len(a)}")

print("\tЗадание 2\nВведите два списка чисел")
ln1 = int(input())
a1 = set()
for i in range(ln1):
    num = int(input())
    a1.add(num)
ln2 = int(input())
a2 = set()
for i in range(ln2):
    num = int(input())
    a2.add(num)
print(f"Количество чисел, присутствующих в обоих списках: {len(a1.intersection(a2))}")

print("\tЗадание 3\nВведите последовательность чисел")
list = input()
list = list.replace(' ', '')
a = set()
for i in list:
    if i in a:
        print(f"{i}: YES")
    else:
        print(f"{i}: NO")
    a.add(i)