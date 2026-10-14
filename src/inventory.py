class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, name, qty):
        if qty < 0:
            raise ValueError('qty must be non-negative')
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_stock(self, name, qty):
        if qty < 0:
            raise ValueError('qty must be non-negative')
        if self.stock.get(name, 0) < qty:
            raise ValueError('not enough stock')
        self.stock[name] -= qty
        if self.stock[name] == 0:
            del self.stock[name]