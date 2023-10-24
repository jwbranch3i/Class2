class FileHandler:
    def __init__(self, filename: str):
        """
        Initialize a FileHandler instance with the provided filename.

        :param filename: The name of the file to be handled.
        """
        self.filename = filename

    def read(self) -> str:
        """
        Read the contents of the file and return it as a string.

        If the file does not exist, return None.

        :return: The file contents as a string, or None if the file does not exist.
        """
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None

    def write(self, data: str) -> None:
        """
        Write the provided data to the file.

        :param data: The data to be written to the file as a string.
        """
        with open(self.filename, "w") as file:
            file.write(data)
