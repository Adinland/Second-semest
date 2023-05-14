print("\tЗадание 2")

def create(pet_dict):
    print("-> Поочерёдно введите кличку животного, вид, возраст и имя владельца")
    pet_name = input()
    pet_kind = input()
    pet_age = int(input())
    pet_owner_name = input()
    pet_dict.update({len(pet_dict) + 1 : {pet_name : {"Вид" : pet_kind, "Возраст" : pet_age, "Владелец" : pet_owner_name}}})

def read(pet_dict):
    if len(pet_dict) == 0:
        print("-> Записи отсутсвуют")
    else:
        print("-> Введите порядковый номер записи")
        num = int(input())
        if len(pet_dict) < num:
            print("-> Запись отсутствует")
        else:
            for i in pet_dict[num]:
                if (pet_dict[num][i].get('Возраст') >= 5 and pet_dict[num][i].get('Возраст') <= 20) or (pet_dict[num][i].get('Возраст') % 10 >= 5 and pet_dict[num][i].get('Возраст') % 10 <=9) or (pet_dict[num][i].get('Возраст') % 10 == 0):
                    suff = "лет"
                elif pet_dict[num][i].get('Возраст') % 10 == 1:
                    suff = "год"
                elif pet_dict[num][i].get('Возраст') % 10 > 1 and pet_dict[num][i].get('Возраст') % 10 < 5:
                    suff = "года"
                print(f"-> Это {pet_dict[num][i].get('Вид')} по кличке {i}. Возраст питомца {pet_dict[num][i].get('Возраст')} {suff}. Имя владельца {pet_dict[num][i].get('Владелец')}")

def update(pet_dict):
    if len(pet_dict) == 0:
        print("-> Записи отсутсвуют")
    else:
        print("-> Введите порядковый номер записи")
        num = int(input())
        if len(pet_dict) < num:
            print("-> Запись отсутствует")
        else:
            exit = False
            while exit != True:
                print("-> Выберите действие:\n\t  1)Изменить кличку\n\t  2)Изменить вид\n\t  3)Изменить возраст\n\t  4)Изменить имя владельца")
                command = input()
                if command == '1':
                    print("-> Введите новое имя")
                    pet_name = input()
                    for i in pet_dict[num]:
                        pet_dict[num] = {pet_name : {"Вид" : pet_dict[num][i].get('Вид'), "Возраст" : pet_dict[num][i].get('Возраст'), "Владелец" : pet_dict[num][i].get('Владелец')}}
                    exit = True
                elif command == '2':
                    print("-> Введите новый вид")
                    pet_kind = input()
                    for i in pet_dict[num]:
                        pet_dict[num] = {i : {"Вид" : pet_kind, "Возраст" : pet_dict[num][i].get('Возраст'), "Владелец" : pet_dict[num][i].get('Владелец')}}
                    exit = True
                elif command == '3':
                    print("-> Введите новый возраст")
                    pet_age = int(input())
                    for i in pet_dict[num]:
                        pet_dict[num] = {i : {"Вид" : pet_dict[num][i].get('Вид'), "Возраст" : pet_age, "Владелец" : pet_dict[num][i].get('Владелец')}}
                    exit = True
                elif command == '4':
                    print("-> Введите новое имя владельца")
                    pet_owner_name = input()
                    for i in pet_dict[num]:
                        pet_dict[num] = {i : {"Вид" : pet_dict[num][i].get('Вид'), "Возраст" : pet_dict[num][i].get('Возраст'), "Владелец" : pet_owner_name}}
                    exit = True
                else:
                    print("-> Ошибка: некорректная команда")

def delete(pet_dict):
    if len(pet_dict) == 0:
        print("-> Записи отсутсвуют")
    else:
        print("-> Введите порядковый номер записи")
        num = int(input())
        if len(pet_dict) < num:
            print("-> Запись отсутствует")
        elif (len(pet_dict) == 1) or (len(pet_dict) == num):
            pet_dict.pop(num)
        elif num < len(pet_dict):
            pet_dict.pop(num)
            for i in range(1, len(pet_dict) + 2):
                if i > num:
                    for j in pet_dict[i]:
                        pet_dict[i - 1] = pet_dict.pop(i)

#проверочные данные
pets = {1:{"Брюч":{"Вид":"Карликовый питон","Возраст": 33,"Владелец":"Саня"}}, 
        2:{"Бирс":{"Вид":"Камышовый кот","Возраст": 21,"Владелец":"Даня"}}, 
        3:{"Бусь":{"Вид":"Дворняга","Возраст": 27,"Владелец":"Гена"}}}#dict()
command = ''
while command != '5':
    print("-> Выберите действие:\n\t1)Создать запись\n\t2)Просмотреть запись\n\t3)Обновить запись\n\t4)Удалить запись\n\t5Выход")
    command = input()
    if command == '1':
        create(pets)
    elif command == '2':
        read(pets)
    elif command == '3':
        update(pets)
    elif command == '4':
        delete(pets)
    elif command == '5':
        print("-> Выход...")
    else:
        print("-> Ошибка: некорректная команда")