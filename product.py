# product.property

# This module defines a data class representing a product.


# The Product class represents a single product item. It uses properties
# and setters for encapsulating the access and modification of certain
# attributes, ensuring that direct manipulation of these attributes can be
# controlled or validated in the future if needed.
class Product:
    """
    A simple data class representing a product.

    Attributes:
    - _product_id: A private attribute that holds the unique identifier for the product.
    - _name: A private attribute that holds the name of the product.
    - _price: A private attribute that holds the price of the product.
    - _quantity: A private attribute that indicates the quantity of the product in stock.
    """

    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        """
        Initialize a Product object with the given attributes.

        :param product_id: The unique identifier for the product as an integer.
        :param name: The name of the product as a string.
        :param price: The price of the product as a float.
        :param quantity: The quantity of the product in stock as an integer.
        """
        # Initialize the Product object with the given attributes.
        self._product_id = product_id  # Setting the product's unique identifier
        self._name = name  # Setting the product's name
        self._price = price  # Setting the product's price
        self._quantity = quantity  # Setting the product's quantity in stock

    @property
    def product_id(self) -> int:
        """
        Get the product's unique identifier.

        :return: The product's unique identifier as an integer.
        """
        return self._product_id

    @property
    def name(self) -> str:
        """
        Get the product's name.

        :return: The product's name as a string.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Set the product's name.

        :param value: The new name for the product as a string.
        """
        # This setter allows the modification of the product's name.
        # It could be extended in the future for validations or other operations.
        self._name = value

    @property
    def price(self) -> float:
        """
        Get the product's price.

        :return: The product's price as a float.
        """
        return self._price

    @property
    def quantity(self) -> int:
        """
        Get the quantity of the product in stock.

        :return: The quantity of the product in stock as an integer.
        """
        return self._quantity
