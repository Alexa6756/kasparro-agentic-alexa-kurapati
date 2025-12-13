import json, os
from templates.faq_template import faq_template
from templates.product_page_template import product_template
from templates.comparison_template import comparison_template

def writer_node(state):
    os.makedirs("outputs", exist_ok=True)

    faq = faq_template(state["parsed_product"], state["questions"])
    product = product_template(state["parsed_product"])
    comparison = comparison_template(state["parsed_product"])

    with open("outputs/faq.json", "w") as f:
        json.dump(faq, f, indent=2)

    with open("outputs/product_page.json", "w") as f:
        json.dump(product, f, indent=2)

    with open("outputs/comparison_page.json", "w") as f:
        json.dump(comparison, f, indent=2)

    state["outputs"] = {
        "faq": faq,
        "product_page": product,
        "comparison_page": comparison
    }
    return state
