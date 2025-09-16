"""
Transformaciones con Map en Diccionarios Complexos

"""

items = [
    {
        "producto": "camisa",
        "price": 100
     #   "taxes": 100 * .19
    },
    {
        "producto": "pantalones",
        "price": 250
    },
    {
        "producto": "zapatos",
        "price": 200
    }
]


def add_taxes(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item

new_items = list(map(add_taxes, items))
print("New list")
print(new_items)
print("Old list")
print(items)