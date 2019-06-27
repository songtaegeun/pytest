i, k, g = 0, 0, ""

#d = int(input("단 입력 : "))

#for i in range(1, 10, 1):
    #print("%d X %d = %2d"%(d, i, d*i))

for i in range(2, 10):
    g = g + ("# %d #" %i)

print(g)


for i in range(1, 10):
    g=""
    for k in range(2, 10):
        g=g+str("%2d X %2d = %2d"%(k, i, k*i))

    print(g)