import unittest
from transformnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("code block", TextType.CODE),
                                TextNode(" word", TextType.TEXT),]
                    )
