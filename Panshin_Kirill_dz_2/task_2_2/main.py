def a(x):
    if x[0] in '+-':
        return x[0]
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(my_list):
    b = a(my_list[i])
    if my_list[i].isdigit() or (b and my_list[i][1:].isdigit()):
        if b:
            my_list[i] = b + my_list[i][1:].zfill(2)
        else:
            my_list[i] = my_list[i].zfill(2)
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    i += 1
print(my_list)
my_list_1 = ' '.join(my_list)
print(my_list_1)
