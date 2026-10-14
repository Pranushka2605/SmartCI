def test_cart_total_intentional_mistake():
    cart = ShoppingCart()
    cart.add_item("Pen", 10, 2)

    # Intentionally incorrect expected result
    assert cart.total() == 50