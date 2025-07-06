from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise AttributeError("no valid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes.append(node)
        else:
           split_node = node.text.split(delimiter)
           if len(split_node) % 2 == 0:
               raise Exception("odd number of delimiters")
           for i in range(len(split_node)):
                if i % 2 == 0:
                    text_nodes.append(TextNode(split_node[i], TextType.TEXT))
                else:
                    text_nodes.append(TextNode(split_node[i], text_type))
    return text_nodes

def main():
    pass
