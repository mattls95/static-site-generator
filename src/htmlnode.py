

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props = ""
        for key, value in self.props.items():
            props += f" {key}={value} " 

    def __eq__(self, node):
        if self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props:
            return True
        return False

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
