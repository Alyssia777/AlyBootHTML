from generate_page import extract_title
import unittest

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        content = """# My Page Title
This is the content of the page.
"""
        title = extract_title(content)
        self.assertEqual(title, "My Page Title")

    def test_extract_title_no_title(self):
        content = """This is the content of the page without a title."""
        with self.assertRaises(ValueError) as context:
            extract_title(content)
        self.assertEqual(str(context.exception), "No title found")