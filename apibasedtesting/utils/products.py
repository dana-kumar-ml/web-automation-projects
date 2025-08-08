def get_product_by_name(api_context, headers, name):
    response = api_context.get("/products", headers=headers)
    assert response.ok, "Failed to fetch products"
    products = response.json()
    return next((p for p in products if p["name"] == name), None)

def add_product_to_cart(api_context, headers, product_id):
    response = api_context.post("/cart", headers=headers, data={
        "product_id": product_id,
        "quantity": 1
    })
    assert response.ok, f"Failed to add product {product_id} to cart"
