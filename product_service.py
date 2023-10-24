from product_repository import ProductRepository
from product_validator import ProductValidator
from product import Product
from constants_messages import ProductMessages


def format_price(price: float):
    """
    Formats the price to two decimal places and adds a dollar sign.

    :param price: The price to format.
    :return: The formatted price as a string (e.g., "$12.34").
    """
    return f"${format(price, '.2f')}"


class ProductService:
    """
    A class that provides business operations related to products.

    Attributes:
    - _repository: An instance of ProductRepository.
    - _validator: An instance of ProductValidator.
    """

    def __init__(self, repository: ProductRepository, validator: ProductValidator):
        """
        Initialize a ProductService instance.

        :param repository: An instance of ProductRepository used to manage product data.
        :param validator: An instance of ProductValidator used to validate product data.
        """
        self._repository = repository
        self._validator = validator

    def list_products(self) -> list:
        """
        List all products available in the repository.

        :return: A list of Product objects.
        """
        return self._repository.list_products()

    def product_exists(self, product_id: int) -> bool:
        """
        Check if a product with the given product ID exists in the repository.

        :param product_id: The ID of the product to check.
        :return: True if the product exists, False otherwise.
        """
        product = self._repository.get_product_by_id(product_id)
        return product is not None

    def add_product(self, product_id: str, name: str, price: str, quantity: str):
        """
        Add a new product to the repository.

        :param product_id: The ID of the new product.
        :param name: The name of the new product.
        :param price: The price of the new product as a string.
        :param quantity: The quantity of the new product as a string.
        :return: A success message if the product is added successfully.
        :raises ProductError: If there is an issue with product data or the product already exists.
        """
        try:
            # 1. Validate the product data.
            (
                valid_id,
                valid_name,
                valid_price,
                valid_quantity,
            ) = self._validate_product_data(product_id, name, price, quantity)

            # 2. Store the product data.
            self._store_new_product(valid_id, valid_name, valid_price, valid_quantity)

            return ProductMessages.PRODUCT_ADDED_SUCCESS
        except ValueError as e:
            raise ProductError(str(e))

    def _validate_product_data(
        self, product_id: str, name: str, price: str, quantity: str
    ):
        # Step 1: Validate product_id first
        valid_id = self._validator.validate_product_id(product_id)
        self._ensure_product_does_not_exist(valid_id)

        # Then validate other attributes
        valid_name = self._validator.validate_product_name(name)
        valid_price = self._validator.validate_product_price(price)
        valid_quantity = self._validator.validate_product_quantity(quantity)

        return valid_id, valid_name, valid_price, valid_quantity

    def _ensure_product_does_not_exist(self, product_id: int):
        if self._repository.get_product_by_id(product_id):
            raise ProductError(ProductMessages.DUPLICATE_PRODUCT_ID)

    def _store_new_product(
        self, valid_id: int, valid_name: str, valid_price: float, valid_quantity: int
    ):
        product = Product(valid_id, valid_name, valid_price, valid_quantity)
        self._repository.add_product(product)
        if not self._repository.get_product_by_id(product.product_id):
            raise ProductError(ProductMessages.ADD_PRODUCT_FAILED)


class ProductError(Exception):
    """Custom exception for product-related issues"""

    pass
