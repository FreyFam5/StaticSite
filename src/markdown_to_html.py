from htmlnode import *
from markdown_to_blocks import *
from inline_markdown import text_to_textnodes
from textnode import *


def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	new_block_nodes = []
	for block in blocks:
		new_block_nodes.append(block_to_html_node(block, block_to_block_type(block)))
	node = ParentNode("div", new_block_nodes)
	return node


def text_to_children(text):
	return list(map(text_node_to_html_node, text_to_textnodes(text)))


def block_to_html_node(block, block_type):
	match block_type:
		# Checks each line and removes it's >, then turns the new combined string into leaf nodes that are added as children in the new quoteblock parent
		case BlockType.QUOTE:
			string_list = []
			lines = block.split("\n")
			for line in lines:
				string_list.append(line[2:] + "<br />")
			new_block = "".join(string_list)
			return ParentNode("blockquote", text_to_children(new_block))
		
		# Just takes the text as is and puts it as a child of the new code parent
		case BlockType.CODE: 
			new_text = block[3:-3].lstrip()
			return ParentNode("pre", [ParentNode("code", [text_node_to_html_node(TextNode(new_text, TextType.TEXT))])])
		
		# Takes the text and removes its new lines and white space, then sets that text to a leaf node that get parented by the new paragraph parent
		case BlockType.PARAGRAPH:
			changed_block = block.strip().replace("\n", " ")
			base_children = text_to_children(changed_block)
			return ParentNode("p", base_children)
		
		# Makes a list of lines that each have their "- " removed and parented to a new li parent, then a list of li's will be added to the new unordered list parent
		case BlockType.UNORDERED_LIST:
			children = []
			lines = block.split("\n")
			for line in lines:
				children.append(ParentNode("li", text_to_children(line[2:])))
			return ParentNode("ul", children)
		
		# Makes a list of lines that each have their "#. " removed and parented to a new li parent, then a list of li's will be added to the new ordered list parent
		case BlockType.ORDERED_LIST:
			children = []
			lines = block.split("\n")
			for line in lines:
				children.append(ParentNode("li", text_to_children(line[3:])))
			return ParentNode("ol", children)
		
		# Checks each # to see how many their are then uses that to set the "<h#>" and how many spaces from the left the new text will start, then it'll be added to the new heading parent
		case BlockType.HEADING:
			found_all = False
			idx = 0
			while found_all == False:
				if block[idx] == "#":
					idx += 1
				else:
					found_all = True
			return ParentNode(f"h{idx}", text_to_children(block[idx + 1:]))