outFp = None
outStr=''
  
outFp = open("./data1.txt","a")
num = 1  
while True:
    outStr=input("입력 내용 : ")
    if outStr != '':
        outFp.writelines(outStr + "\n")
    else:
        break
    num += 1
outFp.close()
