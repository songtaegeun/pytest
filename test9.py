year = 0

if __name__ == "__main__":
    year - int(input("연도 입력 : "))

    if((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print("윤년");
    else:
        print("윤년 아님");