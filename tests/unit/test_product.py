import pytest
import math
from product import Product

def test_product_initialization() -> None:
    """
     Test the initialization of a Product instance.
    """
    product = Product(1, "Test Item 1", 1.05, 50)
    
    assert product.product_id == 1
    assert product.name == "Test Item 1"
    assert abs(product.price - 1.05) <= .0000001
    assert product.quantity == 50

    
def test_product_name_setter() -> None:
    """
    Test the setter for changing the product name.
    """
    # Create a new Product instance
    product = Product(1, "Test Product", 10.99, 100)

    # Change the name using the setter
    product.name = "Updated Product"

    # Verify if the name was correctly updated
    assert product.name == "Updated Product"


@pytest.mark.xfail(reason="Test fails if price is able to be changed.")
def test_product_id_immutable() -> None:
    """
    Test the immutability of the product_id attribute.
    
    Test will fail if product_id is unable to be changed
    """
    product = Product(1, "Test Item 2", 1.05, 50)
     
    product.product_id = 2
    assert product.product_id == 2
    
@pytest.mark.xfail(reason="Test fails if price is able to be changed.")
def test_product_price_immutable() -> None:
    """
    Test the immutability of the price attribute.
    
    Test will pass if price is able to be changed
    """
    # Create a new Product instance
    product = Product(1, "Test Product", 10.99, 100)

    # Try to change the price directly 
    product.price = 12.99
    assert math.isclose(product.price, 12.99)
   
@pytest.mark.xfail(reason="Test fails if quantity is able to be changed.")
def test_product_quantity_immutable() -> None:
    """
    Test the immutability of the quantity attribute.
    
    Test will fail if quantity is unable to be changed
    """
    product = Product(1, "Test Item 2", 1.05, 50)
    product.quantity = 20
    assert product.quantity == 20