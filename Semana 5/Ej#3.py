my_list = [4, 3, 6, 1]
n= len(my_list)

if n >= 4 :
    my_list[0], my_list[1], my_list[-2], my_list[-1] =( my_list[-1], my_list[-2], my_list[1], my_list[0] )
    

print(my_list)