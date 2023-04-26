
print("\tЗадание 1\nВведите две стороны прямоугольника:\na = ", end='')
a = float(input())
print("b = ", end='')
b = float(input())
#a, b = map(int, input().split())
print("S = ", a * b, "\nP = ", 2*a+2*b)

print("\tЗадание 2\nПросто (добавь воды) введите число:")
a = input()
print(float(a[3]) ** float(a[4]) * float(a[2]) / (float(a[0]) - float(a[1])))
