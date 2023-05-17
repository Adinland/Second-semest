def list_out(my_list, num):
    if num < len(my_list):
        print(my_list[num], end=' ')
        list_out(my_list, num + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
list_out(my_list, 1)