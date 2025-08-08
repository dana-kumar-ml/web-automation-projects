# tests/api/test_checkout_flow.py

import pytest
from playwright.sync_api import APIRequestContext
from utils.auth import login_user
from utils.products import get_product_by_name, add_product_to_cart
from utils.cart import get_cart_items
from utils.checkout import checkout_user, verify_checkout_completion

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="session")
def api_context(playwright):
    base_url = "https://www.saucedemo.com/"  # Configurable in real setup
    context = playwright.request.new_context(base_url=base_url)
    yield context
    context.dispose()


@pytest.fixture
def auth_headers(api_context):
    """Log in and return auth headers for API requests."""
    token = login_user(api_context, "standard_user", "secret_sauce")
    return {"Authorization": f"Bearer {token}"}


def test_api_checkout_flow(api_context: APIRequestContext, auth_headers):
    """
    End-to-end checkout flow using API:
    - Login
    - Fetch product
    - Add to cart
    - Verify cart
    - Checkout
    - Verify order success
    """
    logger.info("🔎 Fetching product")
    product = get_product_by_name(api_context, auth_headers, "Sauce Labs Backpack")
    assert product, "Product not found"

    logger.info("➕ Adding product to cart")
    add_product_to_cart(api_context, auth_headers, product_id=product["id"])

    logger.info("🧾 Verifying cart")
    cart_items = get_cart_items(api_context, auth_headers)
    assert any(item["product_id"] == product["id"] for item in cart_items), "Product not in cart"

    logger.info("💳 Performing checkout")
    checkout_user(api_context, auth_headers, "John", "Doe", "12345")

    logger.info("✅ Verifying order completion")
    assert verify_checkout_completion(api_context, auth_headers), "Order did not complete successfully"
