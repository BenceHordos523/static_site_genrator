
from splitter import extract_markdown_links, split_notes_delimiter, extract_markdown_images
from textnode import TextNode, TextType


def main():

    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_notes_delimiter([node], "**", TextType.BOLD)
    
    print(new_nodes)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

    print(extract_markdown_links(text))

main()
