import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockTypes(unittest.TestCase):
    def test_block_type_heading(self):
        heading = "# This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING)

    def test_block_type_unordered_list(self):
        unordered_list = (
                "- This is the first list item in a list block\n"
                "- This is a list item\n"
                "- This is another list item\n"
                        )
        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

    def test_block_type_paragraph(self):
        paragraph = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)
