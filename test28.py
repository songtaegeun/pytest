import operator
# numList = []
# for num in range(1, 6):
#     numList.append(num)

# numList = [num for num in range(1, 6)]
# print(numList)

# oldlist = ['짜장면', "탕수육", "군만두"]
# newlist = []
# newlist = oldlist
# print(newlist)
# oldlist[0] = ["짬뽕"]
# oldlist.append('깐풍기')
# print(newlist)

# oldlist = ['짜장면', "탕수육", "군만두"]
# newlist = []
# newlist = oldlist[:]
# print(newlist)
# oldlist[0] = ["짬뽕"]
# oldlist.append('깐풍기')
# print(newlist)

# ss = "010-3337-2485"
# #print(ss[1:4])
# new = ss.replace("010", '클라우드')
# print(new)
#
# ss = 'aASDsdasdad'
#
# ss = ss.lower()
# print(ss)
# if len(ss) > 8 :
#     print("다시")

inStr = ''' 나아이이이잇 코오오오노 코오오노 DIO가
나는야 바다의 남자 너는 야 ㅎ=태야의 뭐지
ㅁㄴ어ㅏㅣㄴ움림ㅈㅎㄻ더ㅓ루맒
ㄴㅇㄴ루마ㅓㅎ류ㅏ목ㅎ퐏ㅁㄱㄹ묻거ㅏㅁㄷㅎㄱ

'''
countDic = {}
countList = []

if __name__ == "__main__":
    for ch in inStr :

        if '가' <= ch and ch <= "힣":
            if ch in countDic:
                countDic[ch] += 1
            else:
                countDic[ch] = 1

    countList = sorted(countDic.items(), key = operator.itemgetter(1),reverse=True)

    print("원문\n", inStr)
    print("-------------")
    print('문자\t빈도수')
    print('------------')
    for i in range(0, len(countList)):
        print(countList[i][0], '\t',countList[i][1])