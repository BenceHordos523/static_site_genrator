import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node3 = TextNode("This is a text node", TextType.LINK, url="www.google.com")
        node4 = TextNode("This is a text node", TextType.BOLD)

    
        self.assertNotEqual(node3, node4)

    def test_eq_url(self):
        node5 = TextNode("This is a text node", TextType.LINK, url="www.google.com")
        node6 = TextNode("This is a text node", TextType.LINK, url="www.google.com")

        self.assertEqual(node5, node6)




if __name__ == "__main__":
    unittest.main()
