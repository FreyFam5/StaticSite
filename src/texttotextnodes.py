from splitnodes import *
from textnode import *

def text_to_textnodes(text):
	node = TextNode(text, TextType.TEXT)
	new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
	new_nodes = split_nodes_image(new_nodes)
	new_nodes = split_nodes_link(new_nodes)
	return new_nodes