print("\tЗадание 1\nВведите число, затем столько же целых чисел")
arr = []
zeros_count = 0
for i in range(int(input())):
    arr.append(int(input()))
    if arr[i] == 0:
        zeros_count += 1 
print("Список: ", end='')
for i in arr:
    print(i, end=' ')
print("\nКоличество нулей:", zeros_count)

print("\tЗадание 2\nВведите число")
N = int(input())
count = 0
print("Делители:")
for i in range(1, N + 1):
    if N % i == 0:
        count +=1
        print(i, end=' ')

print("\tЗадание 3\nВведите А и В, где А < В")
A = int(input())
B = int(input())
print("Чётные числа на отрезке:")
for i in range(A, B + 1):
    if i % 2 == 0:
        print(i, end=' ')