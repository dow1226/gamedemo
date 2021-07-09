# 商品定義

class Product():

    # 商品初始化
    def __init__(self, name, product_nums, product_price):
        self.name = name
        self.product_nums = product_nums
        self.product_price = product_price

    def product_increase(self, product_nums):
        pass

    def product_sell(self, product_nums, product_price):
        pass