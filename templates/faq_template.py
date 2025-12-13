def faq_template(product, questions):
    return {
        "page": "FAQ",
        "product": product["name"],
        "faqs": [
            {
                "question": q["question"],
                "answer": product["benefits"][0],
                "category": q["category"]
            }
            for q in questions[:5]
        ]
    }
