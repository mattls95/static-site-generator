from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("All leaf nodes must have a value")
        else:
            super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.tag:
            return str(self.value)
        else:
            if not self.props:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props_string = ""
                for key, value in self.props.items():
                    props_string += f'{key}="{value}" '
                return f"<{self.tag} {props_string}>{self.value}</{self.tag}>"

