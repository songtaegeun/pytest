i, hap = 0, 0
num = 0

num = int(input("값을 입력해 주세요 : "))

for i in range(1, num+1, 1):
    hap = hap + i

print("1부터 %d까지의 합계 : %d" % (num, hap))