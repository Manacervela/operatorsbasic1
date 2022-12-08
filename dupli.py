list1 = [1,2,3,4,5,4,3,2,2,1,5]
list2 = [4,5,6,7,8,4,5,6,7,7,8]

# delete duplicate
a = set(list1)
b = set(list2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
inter = list(a & b)