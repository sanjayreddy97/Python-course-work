'''Coin class for coin_counter
Author: Sanjay Reddy Muthyala
'''

class Coin:
    #Constructor
    def __init__(self,name,count,value):
        self.name = name
        self.count = count
        self.value = value

    def getName(self):
        return self.name

    def check_input(self):
        if self.count == None:
            return True

        elif self.count < 0:
            return True

        else:
            return False

    def cal_total(self):
        return self.value * self.count
