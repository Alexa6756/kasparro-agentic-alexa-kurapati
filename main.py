import json
from graph.workflow import build_workflow

PRODUCT_DATA = {
    "Product Name": "GlowBoost Vitamin C Serum",
    "Concentration": "10% Vitamin C",
    "Skin Type": "Oily, Combination",
    "Key Ingredients": "Vitamin C, Hyaluronic Acid",
    "Benefits": "Brightening, Fades dark spots",
    "How to Use": "Apply 2–3 drops in the morning before sunscreen",
    "Side Effects": "Mild tingling for sensitive skin",
    "Price": "₹699"
}

if __name__ == "__main__":
    workflow = build_workflow()
    state = {
        "raw_product_data": json.dumps(PRODUCT_DATA),
        "parsed_product": None,
        "questions": None,
        "outputs": {}
    }
    workflow.invoke(state)
    print("Pipeline completed. Outputs written to /outputs")
