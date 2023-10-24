class IOHandler:
    def input(self, prompt: str) -> str:
        """
        Read user input from the console with the provided prompt.

        :param prompt: The prompt message displayed to the user.
        :return: The user's input as a string.
        """
        return input(prompt)

    def print(self, message: str) -> None:
        """
        Print the provided message to the console.

        :param message: The message to be displayed.
        """
        print(message)
