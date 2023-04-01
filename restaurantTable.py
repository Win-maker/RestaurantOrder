
class RestaurantTable:
    menus = {
    'pizza':5000,
    'cola':2500,
    'apple juice':3000,
    'fried chicken':5000,
    'hambuger':5500
}
    def __init__(self):
        self.order = []
        self.bill = 0
        
    def get_order(self, user_order):
            self.order.append(user_order)
            self.bill += self.menus[user_order]
            
    def showBill(self):
        for order in self.order:
            print(f"{order}: {self.menus[order]}")
        print(f"Total Price is : {self.bill}")
                
def showMenu():
    table = RestaurantTable()
    while True:
        order = input("Order Here  ... ")
        table.get_order(order)
        
        another = input('Order Again ? y/n: y to order, n to exit')
        if another == 'y':
            continue
        elif another == 'n':
            table.showBill()
            break

showMenu()