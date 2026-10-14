from src.pricing import apply_discount, add_tax


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        if qty <= 0:
            raise ValueError('qty must be positive')
        if price < 0:
            raise ValueError('price must be non-negative')
        self.items.append((name, price, qty))

    def total(self, discount=0):
        subtotal = sum(p * q for _, p, q in self.items)
        return add_tax(apply_discount(subtotal, discount))