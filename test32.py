class Car :
    color = ""
    speed = 0

    def __init__(self):
        self.color = "노랑"
        self.speed = 5

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
