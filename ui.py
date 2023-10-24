# ui.py

from abc import ABC, abstractmethod
from product_service import ProductService, format_price, ProductError
from product_validator import ProductValidator
from io_handler import IOHandler
from product_repository import ProductRepository
from data_loader import DataLoader
from file_handler import FileHandler
from constants_messages import ProductMessages, DEFAULT_DATA_FILE


class BaseUI(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def list_products(self):
        pass

    @abstractmethod
    def main_loop(self):
        pass


class CLI(BaseUI):
    def __init__(
        self,
        service: ProductService,
        validator: ProductValidator,
        io_handler: IOHandler,
    ):
        """
        Initialize a CLI (Command Line Interface) instance.

        :param service: An instance of ProductService used for managing product data.
        :param validator: An instance of ProductValidator used for validating product data.
        :param io_handler: An instance of IOHandler for handling input and output operations.
        """
        self._service = service
        self._validator = validator
        self._io = io_handler

        # Menu items defined in a dictionary
        # Each menu item is associated with its corresponding function
        self.menu_items = {
            "Add Product": self.add_product,
            "List Products": self.list_products,
            "Exit": self.exit_app,
        }

    def display_menu(self):
        """
        Display the main menu options.
        """
        self._io.print("\nMenu:")
        for index, item in enumerate(self.menu_items.keys(), start=1):
            self._io.print(f"{index}. {item}")

    def main_loop(self):
        """
        Main loop for the CLI application.
        """
        while True:
            self.display_menu()
            try:
                choice = int(self._io.input("Enter your choice: "))
                # Fetching the function from menu items using the choice and executing it
                selected_func = list(self.menu_items.values())[choice - 1]
                selected_func()
            except (ValueError, IndexError):
                self._io.print("Invalid choice! Please try again.")

    def exit_app(self):
        """
        Exit the application.
        """
        self._io.print("Goodbye!")

    def list_products(self):
        """
        List all products available in the repository.
        """
        products = self._service.list_products()
        if not products:
            self._io.print("No products available.")
            return

        for product in products:
            self._io.print(
                f"ID: {product.product_id} | Name: {product.name} | Price: {format_price(product.price)} | Quantity: {product.quantity}"
            )

    def add_product(self):
        """
        Add a new product to the repository.
        """
        product_id, name, price, quantity = self.get_product_details()
        if product_id and name and price and quantity:
            try:
                result = self._service.add_product(product_id, name, price, quantity)
                if result:  # Only print if result is truthy
                    self._io.print(result)
            except ProductError as pe:
                self._io.print(str(pe))

    def get_product_details(self):
        """
        Get details for a new product from user input.

        :return: A tuple containing product_id, name, price, and quantity.
        """
        product_id = self.input_with_validation(
            "Enter product ID (or press Enter to cancel): ",
            self._validator.validate_product_id,
            ProductMessages.INVALID_INTEGER + " " + ProductMessages.INPUT_VALUE,
        )

        if product_id is None:
            return None, None, None, None

        if self._service.product_exists(product_id):
            self._io.print(
                ProductMessages.DUPLICATE_PRODUCT_ID + " " + ProductMessages.INPUT_VALUE
            )
            return None, None, None, None

        name = self.input_with_validation(
            "Enter product name (or press Enter to cancel): ",
            self._validator.validate_product_name,
            "Invalid product name. Please enter again or press Enter to cancel.",
        )
        if name is None:
            return None, None, None, None

        price = self.input_with_validation(
            "Enter product price (or press Enter to cancel): ",
            self._validator.validate_product_price,
            ProductMessages.INVALID_PRICE + " " + ProductMessages.INPUT_VALUE,
        )
        if price is None:
            return None, None, None, None

        quantity = self.input_with_validation(
            "Enter product quantity (or press Enter to cancel): ",
            self._validator.validate_product_quantity,
            ProductMessages.INVALID_QUANTITY + " " + ProductMessages.INPUT_VALUE,
        )
        if quantity is None:
            return None, None, None, None

        return product_id, name, price, quantity

    def input_with_validation(self, prompt: str, validation_func, error_msg: str):
        """
        Get user input with validation.

        :param prompt: The input prompt message.
        :param validation_func: The validation function to apply to the input.
        :param error_msg: The error message to display on validation failure.
        :return: Validated input value.
        """
        while True:
            value = self._io.input(prompt)
            if not value.strip():
                return None

            try:
                validated_value = validation_func(value)
                return validated_value
            except ValueError as ve:
                self._io.print(str(ve))


# The entry point of the program.
if __name__ == "__main__":
    # Dependency injection is used here for greater flexibility and testability.
    file_handler = FileHandler(DEFAULT_DATA_FILE)
    loader = DataLoader(file_handler)
    repository = ProductRepository(loader)
    validator = ProductValidator()
    io_handler = (
        IOHandler()
    )  # Assuming IOHandler is a separate class for handling input/output operations.
    service = ProductService(repository, validator)
    cli = CLI(service, validator, io_handler)
    cli.main_loop()
