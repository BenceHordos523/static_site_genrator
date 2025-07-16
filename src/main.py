
from splitter import split_notes_delimiter
from textnode import TextNode, TextType


def main():

    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_notes_delimiter([node], "**", TextType.BOLD)
    
    print(new_nodes)





main()
