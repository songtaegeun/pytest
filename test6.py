b = int(input("숫자 입력 : "))
a = "*"

for i in range(0, b, 1):
    for j in range(0, b-i):
        print(" ", end="")
    for k in range(0, (i*2)-1):
        print(a, end="")

    print("")

for i in range(b, 0, -1):
    for j in range(0, b-i):
        print(" ", end="")
    for k in range(0, (i*2)-1):
        print(a, end="")

    print("")

for x in range(1, b*2, 2):
    print((" " * ( (b * 2 -1 - x)//2))+("*" * x ))

for y in range(b * 2-3, 0, -2):
    print((" " * ( (b * 2 -1 - y)//2))+("*" * y ))