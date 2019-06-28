# def func1():
#     global a
#     a = 10
#     print("func1()에서 a값 %d" %a)
#
#
# def func2():
#     print("func2()에서 a값 %d" % a)
#
# a = 20
#
# func1()
# func2()

def telcheck(a):
    re = False
    if len(a) == 11:
        re = True
    return re

if __name__ == "__main__":
    result = False
    # a = 20
    # b = 2
    # print(a)
    # print(b)

    tel1 = "010-488-0"
    tel2 = "01040880116"

    tel1 = tel1.replace("-", '')
    result = telcheck(tel2)

    if result == True:
        print("핸드폰 번화 번호 형식에 맞음")
    else:
        print("형식과 맞지 않음")