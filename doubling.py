# delete doubling on the list

list = [1,2,3,"Anna",2,2,1,"Anna",3]

list = list(set(list))

print(list)