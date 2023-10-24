# constants_messages.py
# Constants and messages related to products are maintained in this file.

# Maximum allowable lengths for product ID and product name.
MAX_PRODUCT_ID_LENGTH: int = 15
MAX_PRODUCT_NAME_LENGTH: int = 30
DEFAULT_DATA_FILE: str = "products.json"


# This class respects the SRP principle by centralizing error messages.
class ProductMessages:
    """
    This class provides centralized messages related to products.

    Static methods provide messages that need to incorporate dynamic values.
    """

    # Error Messages/Product ID
    DUPLICATE_PRODUCT_ID: str = (
        "ERROR: Duplicate product ID! Please choose a unique product ID."
    )
    INVALID_INTEGER: str = "ERROR: Product ID should be a valid integer."
    NON_POSITIVE_ID: str = "ERROR: Product ID should be a positive integer."
    ID_TOO_LONG: str = (
        f"Product ID cannot be longer than {MAX_PRODUCT_ID_LENGTH} characters."
    )

    # Error Messages/Name
    NAME_TOO_LONG: str = f"ERROR: Product Name cannot be longer than {MAX_PRODUCT_NAME_LENGTH} characters."
    EMPTY_NAME: str = "ERROR: Name cannot be empty or just whitespace."

    # Error Messages: Price
    INVALID_PRICE: str = "Product price must be a valid number."
    NON_POSITIVE_PRICE: str = "Product price must be greater than 0."

    # Error Messages/Quantity
    INVALID_QUANTITY: str = "Product quantity must be a valid integer."
    NEGATIVE_QUANTITY: str = "Product quantity cannot be negative."

    # Error Messages/Generic
    ADD_PRODUCT_FAILED: str = "ERROR: Failed to Add Product."

    # Positive/Informative Messages
    PRODUCT_ADDED_SUCCESS: str = "Product added successfully."
    INPUT_VALUE: str = "Please enter again or press Enter to cancel."
