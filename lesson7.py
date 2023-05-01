print("\tЗадание 1\nВведите слово")
word = str(input())
if word[::-1] == word:
    print("Yes")
else:
    print("No")

print("\tЗадание 2\nВведите предложение")
string = str(input())
while string.find('  ') != -1:
    string = string.replace('  ', ' ')
print(string)