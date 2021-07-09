# 玩家定義
class Player():
    
    # 玩家初始化
    def __init__(self, name, sex, age, cash, position):
        self.name = name
        self.sex = sex
        self.age = age
        self.cash = cash
        self.position = position

    # 玩家購買行為
    def buy_target(self, target, target_nums):
        pass

    # 玩家購買行為
    def sell_target(self, target, target_nums):
        pass

    