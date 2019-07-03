inFp = None
inStr = ""
  
inFp = open("./data1.txt","r")
  
while True:
    inStr = inFp.readline()
    if inStr =="":
        break;
    print(inStr , end="")

inFp.close()
