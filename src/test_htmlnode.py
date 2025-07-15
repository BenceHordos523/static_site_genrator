import unittest

from htmlnode import HTMLNode, LeafNode

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

