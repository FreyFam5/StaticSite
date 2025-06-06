from textnode import *

## Takes a list of text nodes and reutrns another list of text nodes that have their correct text types
def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	# Checks each node given
	for node in old_nodes:
		if node.text_type is not TextType.TEXT: # If node isn't text, just returns it
			new_nodes.append(node)
			continue
		# If the amount of delimiters is uneven, will raise an error
		if node.text.count(delimiter) % 2 != 0:
			raise Exception("Uneven amount of delimiters in the given text")
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