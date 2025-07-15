import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
                "a", 
                "In a tag", 
                children=None, 
                props={"href":"https://www.google.com","target":"_blank"})
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


        
