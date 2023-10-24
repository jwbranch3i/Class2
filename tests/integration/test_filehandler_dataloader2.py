import json
import pytest
import os
from data_loader import DataLoader
from file_handler import FileHandler

# Define the path for a temporary file that will be used for testing
TEMP_FILE_PATH = "temp_test_file.json"


# Fixture to create and remove a temporary test file
@pytest.fixture
def test_file():
    """
    Provides a temporary file path and ensures its cleanup after the test.
    """
    yield TEMP_FILE_PATH  # Yield the file path to the test function
    # Cleanup: Remove the temporary file after the test function completes
    if os.path.exists(TEMP_FILE_PATH):
        os.remove(TEMP_FILE_PATH)


# Fixture to provide FileHandler instance
@pytest.fixture
def file_handler(test_file):
    """
    Provides a FileHandler instance initialized with the test_file.
    """
    return FileHandler(test_file)


# Fixture to provide DataLoader instance
@pytest.fixture
def data_loader(file_handler):
    """
    Provides a DataLoader instance initialized with the provided FileHandler.
    """
    return DataLoader(file_handler)

    # def test_integration_dataloader_filehandler():
    """
    Integration test for DataLoader and FileHandler.
    - Test saving data with DataLoader and verify by reading the file directly
    - Test loading data with DataLoader and verify it matches the saved data
    - Test DataLoader's behavior with corrupted data in the file
    """
