s = int(input("입력 : "))

if s >= 90 :
    print("A", end='')
elif s >= 80:
    print("B", end='')
elif s >= 70:
    print("C", end='')
elif s >= 60:
    print("D", end='')
else:
    print("F",end='')

print("학점.")