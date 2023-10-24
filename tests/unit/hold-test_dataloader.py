import json
import pytest
from unittest.mock import Mock
from data_loader import DataLoader

# pytest fixtures are a powerful feature for providing a fixed baseline upon which tests can reliably and repeatedly execute
# Here, we define two fixtures: mock_file_handler and data_loader


# This fixture is used to create a mock object that simulates the behavior of FileHandler
# Mock objects are used to replace real objects in order to isolate the system under test from its environment
@pytest.fixture
def mock_file_handler():
    """
    This fixture creates and returns a mock object that simulates the FileHandler class.
    The mock object is used in place of the real FileHandler to isolate the DataLoader during testing.
    """
    return Mock()


# This fixture creates an instance of DataLoader with the mock_file_handler as its dependency
# This allows us to test DataLoader without relying on the actual implementation of FileHandler
@pytest.fixture
def data_loader(mock_file_handler):
    """
    This fixture creates and returns an instance of DataLoader with mock_file_handler as its dependency.
    """
    return DataLoader(file_handler=mock_file_handler)

    # Below are the test functions, each function tests a specific behavior of the DataLoader class

    # def test_load_data_with_valid_json(mock_file_handler, data_loader):
    """
    Test if DataLoader.load_data() can properly load and return data when the JSON string is valid.
    """

    # def test_load_data_with_invalid_json():
    """
    Test if DataLoader.load_data() returns an empty dictionary when the JSON string is invalid.
    """

    ##def test_save_data():
    """
    Test if DataLoader.save_data() properly converts a dictionary to a JSON string and writes it to a file.
    """
