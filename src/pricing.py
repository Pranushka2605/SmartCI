def apply_discount(price, percent):
    if price < 0:
        raise ValueError('price must be non-negative')
    if 0 <= percent <= 1:
        percent *= 100
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * (1 - percent / 100), 2)


def add_tax(price, rate=0.18):
    if price < 0:
        raise ValueError('price must be non-negative')
    if rate < 0:
        raise ValueError('rate must be non-negative')
    if 1 <= rate <= 100:
        rate /= 100
    return round(price * (1 + rate), 2)