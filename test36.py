import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class car:
    speed = 0

    def upspeed(self, value):
        self.speed += value

        print("현재 속도(슈처 클레스) : %d"%self.speed)


class sedan(car):
    def upspeed(self, value):
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
            print("현재 속도(서브 클레스) : %d"%self.speed)

class truck(car):
      pass

sedan1,truck1 =None,None

truck1 = truck()
sedan1 = sedan()

print("트럭-->",end="")
truck1.upspeed(200)

print("승용차-->",end="")
sedan1.upspeed(150)
