import re
class StringCalculator:
    
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if numbers.startswith("//"):
            delimiter = numbers[2:3]
            numbers = numbers[4:]
            return self._sum_of_numbers(numbers, delimiter)
        return self._sum_of_numbers(numbers, ",\n")
    
    def _sum_of_numbers(self, numbers: str, delimiters: str) -> int:
        numbers_list = re.split(f"[{delimiters}]", numbers)
        
        total = 0
        negative_numbers = []
        
        for num in numbers_list:
            if num:
                value = int(num)
                if value < 0:
                    negative_numbers.append(value)
                else:
                    total += value
        
        if negative_numbers:
            raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
        
        return total

# TDD test class
import unittest

class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newline_delimited_numbers(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3")
        self.assertTrue("negative numbers not allowed" in str(context.exception))

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(self.calc.add("1001,2"), 2)

if __name__ == "__main__":
    unittest.main()
