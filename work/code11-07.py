import os
import shutil

filename = "/var/log/messages"

outFp=None

fh = os.path.isfile(filename)
myStr = "파이썬은 재미 있어요. 파이썬만 매일매일 공부하고 싶어요."
strPosList = []
ctrPosList = []
index = 0
inStr = 0
i= 0
y=0
k = 0
last = 0
tot = len(myStr)
keyword = len("파이썬")

outFp = open("./test1.txt",'w')

while True:
    try:
        index = myStr.index("파이썬",index)
        strPosList.append(index)
        ctrPosList.append(index + 3)
        index = index + 1
    except:
        break
for i in range(0,len(strPosList)):
    if k+1 == len(strPosList):
        outStr += myStr[strPosList[k]+3 : tot]
        print(myStr[strPosList[k]+3 : tot])
    else:
        outStr = myStr[strPosList[k]+3 : strPosList[k+1]-1]
        print(myStr[strPosList[k]+3 : strPosList[k+1]-1])
    k += 1

print("파이썬글자 시작 위치 --> ", strPosList)
print(len(strPosList))#파이썬 글자의수:2
print(len(myStr))#총 길이: 32
print("파이썬글자 끝나는 위치 -->",ctrPosList)
outFp.writelines(outStr)
outFp.close()
#outFp.writelines(myStr.replace("파이썬",""))
