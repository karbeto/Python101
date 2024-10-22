inventory = {
    "apples": 50,
    "bananas": 100,
    "oranges": 75
}


def add_new_product(product, quantity):
    if product not in inventory:
        inventory[product] = quantity
        print(f"Added {product} in inventory")


def update_product_stock(product, quantity):
    if product in inventory:
        inventory[product] += quantity
        print(f"Updated {product} stock to {inventory[product]}")
    else:
        print(f"{product} not found in inventory")


def is_product_out_of_stock(product):
    if inventory.get(product, 0) <= 0:
        print(f"{product} is out of stock")
    else:
        print(f"{product} is in stock with quantity {inventory[product]}")


add_new_product('grapes', 40)
update_product_stock('apples', -20)
is_product_out_of_stock('apples')
