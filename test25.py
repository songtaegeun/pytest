list1 = []
list2 = []
list3 = []
value = 0
result = ''

for i in range(0, 5):
    for k in range(0, 4):
        list1.append(value)
        value += 3
        for j in range(1, 10, 1):
            result = str("%2d x %2d = %2d" % (value, j, value * j))
            list1.append(result)
        list2.append(list1)
        list1 = []
    list3.append(list2)
print(list3)
for i in range(0, 1):
    for k in range(0, 4):
        for j in range(0, 10):
            print(list3[i][k][j])
    print("")



