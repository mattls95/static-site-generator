import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("p")
        node2 = HTMLNode("a")
        self.assertNotEqual(node, node2)

    def test_tag_is_None(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)

    if __name__ == "__main__":
        unittest.main()
