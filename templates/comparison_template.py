def comparison_template(product):
    return {
        "product_a": product["name"],
        "product_b": {
            "name": "GlowMax C Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "price": "₹799"
        },
        "comparison": {
            "price_difference": "GlowBoost is cheaper",
            "ingredient_focus": "GlowBoost is simpler"
        }
    }
