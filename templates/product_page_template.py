def product_template(product):
    return {
        "name": product["name"],
        "price": product["price"],
        "ingredients": product["ingredients"],
        "benefits": product["benefits"],
        "usage": product["usage"]
    }
