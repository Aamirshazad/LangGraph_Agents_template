import unittest
from src.email_assistant.tools import search_files

class TestEmailAssistant(unittest.TestCase):

    def test_search_files(self):
        # Search for the test file in the root directory
        result = search_files.invoke({"directory": ".", "pattern": "test_file.txt"})
        self.assertIn("test_file.txt", result)

if __name__ == '__main__':
    unittest.main()