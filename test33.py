import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


from test32 import Car

myCar = Car()

myCar.color = "Red"
myCar.speed = 20

myCar.upSpeed(40)
myCar.downSpeed(10)


print("자동차의 색상은 %s 이며, 현재 속도는 %dkm입니다" %(myCar.color,myCar.speed))
