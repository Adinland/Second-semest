print("\tЗадание 1\nВведите кличку, вид, возраст, имя владельца")
#проверочные данные
pn = "Змий"#input()
pk = "Ручной гадюк"#input()
pa = 12#int(input())
pon = "Вован-Де-Морт"#input()
pet = {pn:{"Вид":pk, "Возраст":pa, "Владелец":pon}}
for i in pet:
    if (pet[pn].get('Возраст') >=5 and pet[pn].get('Возраст') <= 20) or (pet[pn].get('Возраст') % 10 >= 5 and pet[pn].get('Возраст') % 10 <=9) or (pet[pn].get('Возраст') % 10 == 0):
        end = "лет"
    elif pet[pn].get('Возраст') % 10 == 1:
        end = "год"
    elif pet[pn].get('Возраст') % 10 > 1 and pet[pn].get('Возраст') % 10 < 5:
        end = "года"
    print(f"Это {pet[pn].get('Вид')} по кличке {i}. Возраст питомца {pet[pn].get('Возраст')} {end}. Имя владельца {pet[pn].get('Владелец')}")

print("\tЗадание 2")
my_dict = dict()
for i in range(10, -6, -1):
    my_dict[i] = i**i
    if i >= 0:
        print(f" {i} : {my_dict[i]}")
    else:
        print(f"{i} : {my_dict[i]}")