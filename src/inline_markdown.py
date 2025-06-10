import re
from textnode import TextType, TextNode


def text_to_textnodes(text):
	node = TextNode(text, TextType.TEXT)
	new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
	new_nodes = split_nodes_image(new_nodes)
	new_nodes = split_nodes_link(new_nodes)
	return new_nodes

## Takes a list of text nodes and reutrns another list of text nodes that have their correct text types
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	# Checks each node given
	for node in old_nodes:
		if node.text_type is not TextType.TEXT: # If node isn't text, just returns it
			new_nodes.append(node)
			continue
		temp_array = node.text.split(delimiter)

		node_array = []
		# Checks each text that was split and sets it to the correct given text type
		for idx in range(0, len(temp_array)):
			if temp_array[idx] == "": # Will pass empty strings
				continue
			temp_type = ""
			if idx % 2 == 0: # Text that isn't in the delimiter
				temp_type = node.text_type
			else: # Text that is in the delimiter
				temp_type = text_type
			node_array.append(TextNode(temp_array[idx], temp_type))
		# Adds the fresh nodes to the new nodes
		new_nodes.extend(node_array)
		# Deletes node and old nodes for memory
		del node
	del old_nodes
	return new_nodes

## Splits the nodes with image syntax from the text and creates text nodes for each split text
def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		# If the nodes text is empty, just skip it
		if node.text == "": 
			continue
		# If the node isn't a text object, add it imediatly then continue so it doesn't break
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		split_text = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text) # Returns an array of split text, split at where there is image syntax
		if split_text[0] == node.text: # If the text has not changed, will just return it knowing that their was no image syntax in the text
			new_nodes.append(node)
			continue
		for text in split_text:
			if text == "": # If this text is empty, will just skip
				continue
			extracted_text_array = extract_markdown_images(text) # Extracts the image from the current text
			if len(extracted_text_array) > 0: # If it was able to extract the image then it will create an image text node
				new_nodes.append(TextNode(extracted_text_array[0][0], TextType.IMAGE, extracted_text_array[0][1]))
			else: # Other wise it will just create a normal text node
				new_nodes.append(TextNode(text, TextType.TEXT))
	return new_nodes


## Splits the nodes with link syntax from the text and creates text nodes for each split text
def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		# If the nodes text is empty, just skip it
		if node.text == "": 
			continue
		# If the node isn't a text object, add it imediatly then continue so it doesn't break
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		split_text = re.split(r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))", node.text) # Returns an array of split text, split at where there is link syntax
		if split_text[0] == node.text: # If the text has not changed, will just return it knowing that their was no link syntax in the text
			new_nodes.append(node)
			continue
		for text in split_text:
			if text == "": # If this text is empty, will just skip
				continue
			extracted_text_array = extract_markdown_links(text) # Extracts the link from the current text
			if len(extracted_text_array) > 0: # If it was able to extract the link then it will create an link text node
				new_nodes.append(TextNode(extracted_text_array[0][0], TextType.LINK, extracted_text_array[0][1]))
			else: # Other wise it will just create a normal text node
				new_nodes.append(TextNode(text, TextType.TEXT))
	return new_nodes

## Uses regex to take out the image (![image alt text](https://i.imgur.com/zjjcJKZ.png))
def extract_markdown_images(text):
	return re.findall(r"!\[([^\[\]]*)\]\(([^\)\(]*)\)", text)

## Uses regex to take out the link ([link text](https://bott.dev))
def extract_markdown_links(text):
	return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\)\(]*)\)", text)