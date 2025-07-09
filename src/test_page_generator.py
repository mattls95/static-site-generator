import unittest

from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_extract_title_single_line(self):
        markdown = "# Tolkien Fan Club"
        title = "Tolkien Fan Club"
        self.assertEqual(extract_title(markdown), title)

    def test_extract_title_multiple_lines(self):
        markdown = """
        # Tolkien Fan Club
        # CS Lewis Fan Club
        """
        title = "Tolkien Fan Club"
        self.assertEqual(extract_title(markdown), title)