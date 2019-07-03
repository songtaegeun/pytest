inFp, outFp = None,None
inStr=""

inFp = open("./data1.txt","r")
outFp = open("./data2.txt","w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("-----파일이 복사 되었음------")
