def checkout_user(api_context, headers, first_name, last_name, postal_code):
    response = api_context.post("/checkout", headers=headers, data={
        "first_name": first_name,
        "last_name": last_name,
        "postal_code": postal_code
    })
    assert response.ok, "Checkout failed"


def verify_checkout_completion(api_context, headers):
    response = api_context.get("/checkout/complete", headers=headers)
    if not response.ok:
        return False
    return response.json().get("status") == "success"
