print("\tЗадание 1\nВведите целое число")
num = int(input())
if num > 0:
    if num % 2 != 0:
        print("положительное нечетное число")
    else:
        print("положительное четное число")
elif num < 0:
    if num % 2 != 0:
        print("отрицательное нечетное число")
    else:
        print("отрицательное четное число")
else:
    print("нулевое число")

print("\tЗадание 2\nВведите слово из маленьких латинских букв")
word = str(input())
vowels = 0 #гласные
ltr_a = 0
ltr_e = 0
ltr_i = 0
ltr_o = 0
ltr_u = 0
for i in word:
    if i == 'a':
        ltr_a += 1
        vowels += 1
    elif i == 'e':
        ltr_e += 1
        vowels += 1
        print("BRE")
    elif i == 'i':
        ltr_i += 1
        vowels += 1
    elif i == 'o':
        ltr_o += 1
        vowels += 1
    elif i == 'u':
        ltr_u += 1
        vowels += 1
print("Гласных - ", vowels, "\nСогласных - ", len(word) - vowels)
print("a = ", ltr_a if ltr_a > 0 else "False")
print("e = ", ltr_e if ltr_e > 0 else "False")
print("i = ", ltr_i if ltr_i > 0 else "False")
print("o = ", ltr_o if ltr_o > 0 else "False")
print("u = ", ltr_u if ltr_u > 0 else "False")
#Можно в одном, но так удобоваримо

print("\tЗадание 2\nВведите сумму стартапа, затем бюджет Майкла и Ивана")
amount = float(input())
M_sum = float(input())
I_sum = float(input())
if (M_sum >= amount) & (I_sum >= amount):
    print("2")
elif (M_sum < amount) & (I_sum >= amount):
    print("Иван")
elif (M_sum >= amount) & (I_sum < amount):
    print("Майкл")
elif (M_sum + I_sum) >= amount:
    print("1")
elif (M_sum + I_sum) < amount:
    print("0")