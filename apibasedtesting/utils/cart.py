def get_cart_items(api_context, headers):
    response = api_context.get("/cart", headers=headers)
    assert response.ok, "Failed to fetch cart"
    return response.json()
