import pytest
from product_validator import ProductValidator
from constants_messages import (
    ProductMessages,
    MAX_PRODUCT_ID_LENGTH,
    MAX_PRODUCT_NAME_LENGTH,
)

# Directly initialize the validator instance.
validator = ProductValidator()


def test_validate_product_id_valid():
    """Test if the validator can validate a correct product ID"""
    assert validator.validate_product_id("1") == 1


def test_validate_product_id_non_integer():
    """Test if the validator raises an error for a non-integer product ID"""
    with pytest.raises(ValueError, match=ProductMessages.INVALID_INTEGER):
        validator.validate_product_id("abc")

    # def test_validate_product_id_with_try_except():
    """An example showcasing the use of try-except for testing"""

    # def test_validate_product_id_too_long():
    """Test if the validator raises an error for an overly long product ID"""

    # def test_validate_product_id_non_positive():
    """Test if the validator raises an error for a non-positive product ID"""

    # def test_validate_product_name_valid():
    """Test if the validator can validate a correct product name"""

    # def test_validate_product_name_empty():
    """Test if the validator raises an error for an empty product name"""


def test_validate_product_name_too_long():
    """Test if the validator raises an error for an overly long product name"""
    long_name = "a" * (MAX_PRODUCT_NAME_LENGTH + 1)
    with pytest.raises(ValueError, match=ProductMessages.NAME_TOO_LONG):
        validator.validate_product_name(long_name)

    # def test_validate_product_price_valid():
    """Test if the validator can validate a correct product price"""

    # def test_validate_product_price_invalid():
    """Test if the validator raises an error for an invalid product price"""


def test_validate_product_price_non_positive():
    """Test if the validator raises an error for a non-positive product price"""
    with pytest.raises(ValueError, match=ProductMessages.NON_POSITIVE_PRICE):
        validator.validate_product_price("-10")

    # def test_validate_product_quantity_valid():
    """Test if the validator can validate a correct product quantity"""

    # def test_validate_product_quantity_invalid():
    """Test if the validator raises an error for an invalid product quantity"""


def test_validate_product_quantity_negative():
    """Test if the validator raises an error for a negative product quantity"""
    with pytest.raises(ValueError, match=ProductMessages.NEGATIVE_QUANTITY):
        validator.validate_product_quantity("-10")