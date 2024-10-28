import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from file_search import main  # Assuming the original code is saved in file_search.py

class TestFileSearchMain(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_found(self, mock_stdout):
        # Setting up mock command-line arguments
        test_directory = os.getcwd()
        test_file_name = "test_file.txt"

        # Create a test file
        with open(test_file_name, 'w') as f:
            f.write("This is a test file.")

        with patch.object(sys, 'argv', ["file_search.py", test_directory, test_file_name]):
            main()  # Run the main function with patched arguments
            output = mock_stdout.getvalue().strip()
        
        # Verify output contains the full path to the test file
        self.assertIn(f"File found at: {os.path.join(test_directory, test_file_name)}", output)

        # Cleanup
        os.remove(test_file_name)

    @patch("sys.stdout", new_callable=StringIO)
    def test_file_not_found(self, mock_stdout):
        # Setting up mock command-line arguments
        test_directory = os.getcwd()
        test_file_name = "non_existent_file.txt"

        with patch.object(sys, 'argv', ["file_search.py", test_directory, test_file_name]):
            main()
            output = mock_stdout.getvalue().strip()
        
        # Verify output for file not found
        self.assertEqual(output, "File not found.")

    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_directory(self, mock_stdout):
        # Setting up mock command-line arguments
        invalid_directory = "non_existent_directory"
        test_file_name = "any_file.txt"

        with patch.object(sys, 'argv', ["file_search.py", invalid_directory, test_file_name]):
            main()
            output = mock_stdout.getvalue().strip()
        
        # Verify output for invalid directory
        self.assertEqual(output, f"Invalid directory path: {invalid_directory}")

    @patch("sys.stdout", new_callable=StringIO)
    def test_insufficient_arguments(self, mock_stdout):
        # Setting up mock command-line arguments with only one argument
        with patch.object(sys, 'argv', ["file_search.py", "only_one_argument"]):
            main()
            output = mock_stdout.getvalue().strip()
        
        # Verify output for insufficient arguments
        self.assertEqual(output, "Usage: python file_search.py <directory> <filename>")

if __name__ == "__main__":
    unittest.main()
