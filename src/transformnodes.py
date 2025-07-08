from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode
from extractmarkdown import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_text = node.text
            images = extract_markdown_images(node.text)
            for image in images:
                section = current_text.split(f"![{image[0]}]({image[1]})", 1)
                if section[0]:
                    new_nodes.append(TextNode(section[0], TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                current_text = section[1]
            if current_text:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_text = node.text
            links = extract_markdown_links(node.text)
            for link in links:
                section = current_text.split(f"[{link[0]}]({link[1]})", 1)
                if section[0]:
                    new_nodes.append(TextNode(section[0], TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                current_text = section[1]
            if current_text:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_text_nodes(text):
    text_node = TextNode(text=text, text_type=TextType.TEXT)
    text_nodes =[text_node]

    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks_strip = []
    for block in blocks:
        if len(block.strip()) != 0:
            blocks_strip.append(block.strip())
    return blocks_strip