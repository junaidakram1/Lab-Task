import unittest
from string_permutations import generate_permutations  # Adjusted import statement

class TestGeneratePermutations(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(sorted(generate_permutations("abc")), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(generate_permutations("ab")), sorted(['ab', 'ba']))
        self.assertEqual(sorted(generate_permutations("a")), sorted(['a']))
    
    def test_empty_string(self):
        with self.assertRaises(ValueError) as context:
            generate_permutations("")
        self.assertEqual(str(context.exception), "Input string cannot be empty.")

    def test_none_input(self):
        with self.assertRaises(ValueError) as context:
            generate_permutations(None)
        self.assertEqual(str(context.exception), "Input string cannot be None.")

    def test_single_character(self):
        self.assertEqual(generate_permutations("x"), ['x'])

    def test_duplicate_characters(self):
        self.assertEqual(sorted(generate_permutations("aab")), sorted(['aab', 'aba', 'baa']))

if __name__ == "__main__":
    unittest.main()
