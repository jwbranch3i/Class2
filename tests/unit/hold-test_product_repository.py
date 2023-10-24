import pytest
from unittest.mock import Mock
from product_repository import ProductRepository

# Mock the DataLoader for isolation


@pytest.fixture
def mock_data_loader() -> Mock:
    """
    Fixture to provide a mock instance of DataLoader.

    :return: Mocked instance of DataLoader.
    """
    mock = Mock()
    mock.load_data.return_value = {}  # Default to an empty dict
    return mock


@pytest.fixture
def mock_product() -> Mock:
    """
    Fixture to provide a mock product object with predefined attributes.

    :return: Mocked product instance.
    """
    product = Mock()
    product.product_id = 123
    product.name = "Test Product"
    product.price = 10.5
    product.quantity = 5
    return product

    # def test_load_products(mock_data_loader: Mock, mock_product: Mock) -> None:
    """
    Test to check if products are loaded correctly from the repository using mock objects.

    :param mock_data_loader: Mocked instance of DataLoader.
    :param mock_product: Mocked product instance.
    """

    # def test_add_product() -> None:
    """
    Test to check if products are added correctly to the repository using mock objects.

    :param mock_data_loader: Mocked instance of DataLoader.
    :param mock_product: Mocked product instance.
    """
