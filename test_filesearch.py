import os
import unittest
from task01 import search_files

class TestFileSearch(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        
        self.files_to_create = [
            os.path.join(self.test_dir, 'example01.txt'),
            os.path.join(self.test_dir, 'example02.txt'),
            os.path.join(self.test_dir, 'data.csv'),
            os.path.join(self.test_dir, 'subdir', 'list.docx'),
            os.path.join(self.test_dir, 'subdir', 'data.csv')
        ]
        
        for file_path in self.files_to_create:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write("Sample content")

    def tearDown(self):
        """Clean up the directory structure after tests."""
        for file_path in self.files_to_create:
            if os.path.exists(file_path):  # Check if file exists before removing
                os.remove(file_path)
        subdir_path = os.path.join(self.test_dir, 'subdir')
        if os.path.exists(subdir_path):  # Check for subdir
            os.removedirs(subdir_path)
        if os.path.exists(self.test_dir):  # Check for test dir
            os.rmdir(self.test_dir)

    def test_single_file_search(self):
        result = search_files(self.test_dir, ['example01.txt'], case_sensitive=True)
        self.assertIn('example01.txt', result)
        self.assertEqual(len(result['example01.txt']), 1)
        self.assertIn(os.path.join(self.test_dir, 'example01.txt'), result['example01.txt'])

    def test_multiple_files_search(self):
        result = search_files(self.test_dir, ['data.csv'], case_sensitive=True)
        self.assertEqual(len(result['data.csv']), 2)

    def test_case_insensitive_search(self):
        result = search_files(self.test_dir, ['EXAMPLE02.TXT'], case_sensitive=False)
        self.assertIn('example02.txt', result)
        self.assertEqual(len(result['example02.txt']), 1)

    def test_file_not_found(self):
        result = search_files(self.test_dir, ['nonexistent.txt'], case_sensitive=True)
        self.assertEqual(len(result['nonexistent.txt']), 0)

    def test_directory_not_found(self):
        import io
        import sys
        
        # Redirect stdout to capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        search_files('nonexistent_directory', ['example01.txt'])
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Check if the output contains the expected message
        self.assertIn("The specified directory 'nonexistent_directory' does not exist.", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
