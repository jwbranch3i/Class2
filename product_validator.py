from constants_messages import (
    MAX_PRODUCT_ID_LENGTH,
    MAX_PRODUCT_NAME_LENGTH,
    ProductMessages,
)


class ProductValidator:
    """
    A class dedicated to validating product attributes.

    It raises ValueErrors with specific messages if validation fails.
    """

    def validate_product_id(self, product_id: str) -> int:
        """
        Validate a product ID.

        :param product_id: The product ID to validate as a string.
        :return: The validated product ID as an integer.
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        # Check if product_id is a valid integer
        try:
            id_value = int(product_id)
        except ValueError:
            raise ValueError(ProductMessages.INVALID_INTEGER)

        # Convert the product_id to a string to check its length
        if len(str(id_value)) > MAX_PRODUCT_ID_LENGTH:
            raise ValueError(ProductMessages.ID_TOO_LONG)

        if id_value <= 0:
            raise ValueError(ProductMessages.NON_POSITIVE_ID)

        return id_value

    def validate_product_name(self, name: str) -> str:
        """
        Validate a product name.

        :param name: The product name to validate as a string.
        :return: The validated product name as a string.
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        name = name.strip()
        if not name:
            raise ValueError(ProductMessages.EMPTY_NAME)

        if len(name) > MAX_PRODUCT_NAME_LENGTH:
            raise ValueError(ProductMessages.NAME_TOO_LONG)

        return name

    def validate_product_price(self, price: str) -> float:
        """
        Validate a product price.

        :param price: The product price to validate as a string.
        :return: The validated product price as a float (rounded to 2 decimal places).
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            price_value = float(price)
        except ValueError:
            raise ValueError(ProductMessages.INVALID_PRICE)

        if price_value <= 0:
            raise ValueError(ProductMessages.NON_POSITIVE_PRICE)

        # Round to 2 decimal places
        return round(price_value, 2)

    def validate_product_quantity(self, quantity: str) -> int:
        """
        Validate a product quantity.

        :param quantity: The product quantity to validate as a string.
        :return: The validated product quantity as an integer.
        :raises ValueError: If validation fails, with an appropriate error message.
        """
        try:
            quantity_value = int(quantity)
        except ValueError:
            raise ValueError(ProductMessages.INVALID_QUANTITY)

        if quantity_value < 0:
            raise ValueError(ProductMessages.NEGATIVE_QUANTITY)

        return quantity_value
