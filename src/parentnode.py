from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent node must have a tag")
        if not self.children:
            raise ValueError("parent node must have a children node")
        else:
            parent_node_string = f"<{self.tag}>"
            for child in self.children:
                parent_node_string += child.to_html()
            return f"{parent_node_string}</{self.tag}>"    
