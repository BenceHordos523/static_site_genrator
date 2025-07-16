class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        return_string = ""
        for prop in self.props:
            return_string += f" {prop}=\"{self.props[prop]}\""
        return return_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value can't be None")

        if self.tag is None:
            return self.value 

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag can't be None")

        if self.children is None:
            raise ValueError("children can't be None")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()


        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

