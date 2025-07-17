import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from splitter import extract_markdown_images
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
                "a", 
                "In a tag", 
                None, 
                {"href":"https://www.google.com","target":"_blank"})
        to_html = node.props_to_html()
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", to_html)
    
    def test_not_eq(self):
        node = HTMLNode(
                "a", 
                "In a tag", 
                children=None, 
                props={"href":"https://www.google.com"})
        to_html = node.props_to_html()
        self.assertNotEqual(" href=\"https://www.google.com\" target=\"_blank\"", to_html)

    def test_leaf_to_html_p(self):
        node = LeafNode("p","Hello World!")
        self.assertEqual(node.to_html(),"<p>Hello World!</p>")
    
    def test_leaf_to_html_p2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),"<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span","child")
        parent_node = ParentNode("div",[child_node])
        self.assertEqual(parent_node.to_html(),"<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grand_child = LeafNode("b", "child")
        child_node = ParentNode("span",[grand_child])
        parent_node = ParentNode("div",[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>child</b></span></div>",
        )
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")

        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
