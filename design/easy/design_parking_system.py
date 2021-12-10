class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_space = big
        self.medium_space = medium
        self.small_space = small

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.big_space>=1:
            self.big_space-=1
            return True
        elif carType == 2 and self.medium_space>=1:
            self.medium_space-=1
            return True
        elif carType == 3 and self.small_space>=1:
            self.small_space-=1
            return True
        else:
            return False