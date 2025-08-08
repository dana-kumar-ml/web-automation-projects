def login_user(api_context, username, password):
    response = api_context.post("/login", data={"username": username, "password": password})
    assert response.ok, f"Login failed with status {response.status}"
    token = response.json().get("token")
    assert token, "No token returned during login"
    return token
