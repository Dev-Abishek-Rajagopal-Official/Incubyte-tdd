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
        
        if numbers.startswith("//"):
            return self._handle_custom_delimiters(numbers)
        
        return self._handle_default_delimiters(numbers)

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

        Raises:
            ValueError: An exception for negative values
        """
        num_list = [int(i) for i in re.split(delimiter, numbers) if int(i) < 1001]  

        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(num_list)
    
    def _handle_custom_delimiters(self, numbers: str) -> int:
        """
        Handles input with custom delimiters specified at the beginning.

        Args:
            numbers (str): Input string with custom delimiter notation.

        Returns:
            int: The sum of the numbers.
        """
        match = re.match(r"//(\[.*?\]|\S+)\n(.*)", numbers)
        if match:
            delimiter_part, numbers = match.groups()
            delimiters = re.findall(r"\[(.*?)\]", delimiter_part)  

            if not delimiters:  
                delimiters = [delimiter_part]

            delimiter = "|".join(map(re.escape, delimiters))  

            return self._calculate_sum(numbers, delimiter)

        return self._handle_default_delimiters(numbers)


