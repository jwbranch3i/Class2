import pytest
import os
import json

from file_handler import FileHandler
from data_loader import DataLoader


@pytest.fixture
def test_file() -> str:
    """
    Fixture to provide a test file path and clean it up after the test.

    :return: The path to the test file.
    """
    test_file = "integration_test_data.json"
    yield test_file
    if os.path.exists(test_file):
        os.remove(test_file)


@pytest.fixture
def file_handler(test_file: str) -> FileHandler:
    """
    Fixture to provide an instance of FileHandler with the test file.

    :param test_file: The path to the test file.
    :return: An instance of FileHandler.
    """
    return FileHandler(test_file)


@pytest.fixture
def data_loader(file_handler: FileHandler) -> DataLoader:
    """
    Fixture to provide an instance of DataLoader with the provided FileHandler.

    :param file_handler: An instance of FileHandler to be passed to DataLoader.
    :return: An instance of DataLoader.
    """
    return DataLoader(file_handler)


# Integration Tests


def test_file_handler_and_data_loader_integration(
    data_loader: DataLoader, test_file: str
) -> None:
    """
    Integration test to check if the DataLoader and FileHandler classes work well together.

    :param data_loader: An instance of DataLoader.
    :param test_file: The path to the test file.
    """
    # Prepare some dummy data
    data_to_save = {"1": {"name": "Test Product", "price": 12.5, "quantity": 5}}

    # Use DataLoader to save data
    data_loader.save_data(data_to_save)

    with open(test_file, "r") as file:
        saved_data = json.load(file)
        assert saved_data == data_to_save

    # Use DataLoader to read data back into our application.
    loaded_data = data_loader.load_data()
    assert loaded_data == data_to_save

    # Manually corrupt the json file to simulate a broken or badly formatted data file.
    with open(test_file, "w") as file:
        file.write("corrupt data")

    # When DataLoader encounters the corrupted data file, it should return an empty dictionary.
    loaded_data = data_loader.load_data()
    assert loaded_data == {}
