from textnode import TextNode, TextType


def split_notes_delimiter(old_nodes, delimiter, text_type):
    if len(old_nodes) == 0 or old_nodes is None:
        return None

    result_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            result_nodes.append(node)
        else:
            split_nodes = []
            sections = node.text.split(delimiter)
            print(sections)
            if len(sections) % 2 == 0:
                raise Exception("Invalid markdown, formatted section not closed")
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))
        result_nodes.extend(split_nodes)
    return result_nodes



