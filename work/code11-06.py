import os
import shutil

chk = os.path.isdir("./Park-Dir")

if chk == True :
    o = input("정말로 삭제 하시겠습니까. y/u")
    if o == 'y':
        shutil.rmtree("./Park-Dir")
    else: 
        print("삭제 실패")

else:
    os.mkdir("./Park-Dir")
    os.mkdir("./Park-Dir/test")
