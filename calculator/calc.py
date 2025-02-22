"String Calculator Class"

import re

class StringCalculator:
    """
    A simple string calculator that adds numbers provided in a delimited string.
    """

    def add(self, numbers: str) -> int:
        """
        Adds numbers from a given string.

        Args:
            numbers (str): A string containing numbers separated by a delimiter.

        Returns:
            int: The sum of the numbers. Returns 0 for an empty string.
        """
        if not numbers:
            return 0 
        return self._handle_default_delimiters(numbers=numbers)

    def _handle_default_delimiters(self, numbers: str) -> int:
        """
        Handles default delimiters.

        Args:
            numbers (str): A string containing numbers separated by delimiters.

        Returns:
            int: The sum of the numbers.
        """
        delimiter = r",|\n|\|"
        return self._calculate_sum(numbers=numbers, delimiter=delimiter) 
    
    def _calculate_sum(self, numbers: str, delimiter: str) -> int:
        """
        Splits the input string using the given delimiter and calculates the sum.

        Args:
            numbers (str): A string containing numbers.
            delimiter (str): The delimiter used to separate numbers.

        Returns:
            int: The sum of the parsed numbers.
        """
        num_list = [int(i) for i in re.split(delimiter, numbers)]
        return sum(num for num in num_list)

    
# calc = StringCalculator()
# print(calc.add(input()))
