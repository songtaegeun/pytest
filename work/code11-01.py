inFp = None
inStr = ""

inFp = open("./data1.txt","r")

inStr = inFp.readline()
print(inStr , end="")

inStr = inFp.readline()
print(inStr , end="")

inStr = inFp.readline()
print(inStr , end="")

inFp.close()
