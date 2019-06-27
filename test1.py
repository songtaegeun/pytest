# 변수 선언 부분#
i, k, heartNum = 0, 0, 0
numStr, ch, heartStr = "", "", ""

print("Start")

# 메인 코드#
if __name__ == "__main__": #이 프로그램의 메인
    numStr = input("숫자를 여러 개 입력하세요 : ")
    print("")
    i = 0
    ch = numStr[i]

    while True:
        heartNum = int(ch)

        heartStr = ""
        for k in range(0, heartNum):
            heartStr += "\u2665"
            k += 1

        print(heartStr)

        i += 1
        if (i > len(numStr) - 1):
            break

        ch = numStr[i]

print("end")