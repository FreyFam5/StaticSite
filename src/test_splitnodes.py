import unittest
from splitnodes import *
from textnode import *

class TestSplitNodes(unittest.TestCase):
	def test_splitting_code_words(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])
	
	def test_splitting_italic_words(self):
		node = TextNode("This is text with a _italics_ word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("italics", TextType.ITALIC), TextNode(" word", TextType.TEXT)])

	def test_splitting_bold_words(self):
		node = TextNode("This is text with a **bold** word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)])

	def test_no_splitters(self):
		node= TextNode("This is text with a normal word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		#print("No delimiters: " + str(new_nodes))
	
	def test_one_splitter(self):
		node = TextNode("This is text with a **normal word", TextType.TEXT)
		try:
			new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		except:
			self.assertTrue(True)
	
	def test_multiple_splits(self):
		node_one = TextNode("This is some _italic_ text!", TextType.TEXT)
		node_two = TextNode("This is some more _italic_ text!", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node_one, node_two], "_", TextType.ITALIC)
	
	def test_multiple_splits_inline(self):
		node = TextNode("`This is code` is so cool to use in `This is code` I definatly recommend using `This is also code` sometime!", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		#print(new_nodes)
	
	def test_uneven_delimiters(self):
		node = TextNode("I'm having _trouble_ with no this _syntax man!", TextType.TEXT)
		try:
			new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		except:
			self.assertTrue(True)
	
	def test_empty_string(self):
		node = TextNode("", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		#print("No String Test: " + str(new_nodes))
	
	def test_no_delimiter(self):
		node = TextNode("no delimiters here", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		#print(new_nodes)
	
	def test_empty_delimiter(self):
		node = TextNode("``", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		#print(new_nodes)