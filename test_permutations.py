import unittest
from task02 import generate_permutations, get_all_permutations  # Assuming the main code is in permutations.py

class TestPermutationFunctions(unittest.TestCase):

    def test_empty_string(self):
        # Test for an empty string
        self.assertEqual(generate_permutations(""), [])
        self.assertEqual(get_all_permutations(""), [])

    def test_single_character(self):
        # Test for a single character
        self.assertEqual(generate_permutations("a"), ["a"])
        self.assertEqual(get_all_permutations("a"), ["a"])

    def test_two_characters(self):
        # Test for two distinct characters
        expected = ["ab", "ba"]
        result_recursive = generate_permutations("ab")
        result_iterative = get_all_permutations("ab")
        self.assertEqual(sorted(result_recursive), sorted(expected))
        self.assertEqual(sorted(result_iterative), sorted(expected))

    def test_duplicate_characters_exclude_duplicates(self):
        # Test for duplicate characters with duplicates excluded
        expected = ["aa"]
        result_recursive = generate_permutations("aa", include_duplicates=False)
        result_iterative = get_all_permutations("aa", include_duplicates=False)
        self.assertEqual(result_recursive, expected)
        self.assertEqual(result_iterative, expected)

    def test_duplicate_characters_include_duplicates(self):
        # Test for duplicate characters with duplicates included
        expected = ["aa"]
        result_recursive = generate_permutations("aa", include_duplicates=True)
        result_iterative = get_all_permutations("aa", include_duplicates=True)
        self.assertEqual(result_recursive, expected)
        self.assertEqual(result_iterative, expected)

    def test_three_characters_with_duplicates(self):
        # Test for three characters, two of which are duplicates
        expected = ["aab", "aba", "baa"]
        result_recursive = generate_permutations("aab", include_duplicates=False)
        result_iterative = get_all_permutations("aab", include_duplicates=False)
        self.assertEqual(sorted(result_recursive), sorted(expected))
        self.assertEqual(sorted(result_iterative), sorted(expected))

    def test_large_string_recursive_performance(self):
        # Test performance of the recursive approach with a moderate-length string
        result_recursive = generate_permutations("abcdef")
        self.assertTrue(len(result_recursive) > 0, "Recursive approach failed for 6 characters")

    def test_large_string_iterative_performance(self):
        # Test performance of the iterative approach with a moderate-length string
        result_iterative = get_all_permutations("abcdef")
        self.assertTrue(len(result_iterative) > 0, "Iterative approach failed for 6 characters")


if __name__ == "__main__":
    unittest.main()
