from data_loader import DataLoader
from product import Product
from typing import Dict, List, Optional


class ProductRepository:
    """
    A class that represents a repository of products.

    Attributes:
    - _products: A dictionary to store product objects by their IDs.
    - _loader: An instance of DataLoader class.
    """

    def __init__(self, loader: DataLoader):
        """
        Initialize a ProductRepository instance.

        :param loader: An instance of DataLoader used to load and save product data.
        """
        self._products: Dict[int, Product] = {}
        self._loader: DataLoader = loader
        self._load_products()

    def _load_products(self) -> None:
        """
        Load products from the data source using the DataLoader.
        """
        data: Dict[str, Dict[str, str]] = self._loader.load_data()
        for product_id, product_data in data.items():
            product = Product(
                int(product_id),
                product_data["name"],
                float(product_data["price"]),
                int(product_data["quantity"]),
            )
            self._products[product.product_id] = product

    def add_product(self, product: Product) -> None:
        """
        Add a product to the repository.

        :param product: The product to be added.
        """
        self._products[product.product_id] = product
        self._save_products()

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Get a product from the repository by its ID.

        :param product_id: The ID of the product to retrieve.
        :return: The product with the specified ID or None if not found.
        """
        return self._products.get(product_id)

    def _save_products(self) -> None:
        """
        Save products to the data source using the DataLoader.
        """
        data = {
            str(product_id): {
                "name": product.name,
                "price": str(product.price),
                "quantity": str(product.quantity),
            }
            for product_id, product in self._products.items()
        }
        self._loader.save_data(data)

    def list_products(self) -> List[Product]:
        """
        List all products in the repository.

        :return: A list of all products.
        """
        return list(self._products.values())
