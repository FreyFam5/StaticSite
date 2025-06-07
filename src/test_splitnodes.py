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
	
	## Testing split nodes images
	def test_split_images(self):
		node = TextNode(
		"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
						"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_no_images(self):
		node = TextNode(
		"This is text without an image and another not image",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual([node], new_nodes)
	
	def test_no_string_images(self):
		node = TextNode(
		"",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual([], new_nodes)
	
	def test_incorrect_syntax_images(self):
		node = TextNode(
		"This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual([node], new_nodes)
	
	def test_mix_incorrect_correct_syntax_images(self):
		node = TextNode(
		"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
			],
			new_nodes,
		)
	
	def test_beginning_end_images(self):
		node = TextNode(
		"![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
						"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)
	
	def test_multiple_together_images(self):
		node = TextNode(
		"Images: ![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)![image](https://i.imgur.com/zjjcJKZ.png)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("Images: ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(
						"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes,
		)
	
	def test_split_not_text_images(self):
		nodes = [
			TextNode("This is code", TextType.CODE),
			TextNode("This is bold", TextType.BOLD),
			TextNode("This is italic", TextType.ITALIC),
			TextNode("This is text and an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
			TextNode("This is link", TextType.LINK, "https://boot.dev"),
			TextNode("This is image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
		]
		new_nodes = split_nodes_image(nodes)
		self.assertListEqual(
			[
				TextNode("This is code", TextType.CODE),
				TextNode("This is bold", TextType.BOLD),
				TextNode("This is italic", TextType.ITALIC),
				TextNode("This is text and an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode("This is link", TextType.LINK, "https://boot.dev"),
				TextNode("This is image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes
		)

	## Testing split nodes links
	def test_split_links(self):
		node = TextNode(
		"This is text with an [link](https://i.imgur.com) and another [second link](https://i.imgur.com)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
						"second link", TextType.LINK, "https://i.imgur.com"
				),
			],
			new_nodes,
		)
	
	def test_no_links(self):
		node = TextNode(
		"This is text without an link and another not link",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual([node], new_nodes)
	
	def test_no_string_links(self):
		node = TextNode(
		"",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual([], new_nodes)
	
	def test_incorrect_syntax_links(self):
		node = TextNode(
		"This is text with an ![link](https://i.imgur.com) and another ![second link](https://i.imgur.com)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual([node], new_nodes)
	
	def test_mix_incorrect_correct_syntax_links(self):
		node = TextNode(
		"This is text with an [link](https://i.imgur.com) and another ![second link](https://i.imgur.com)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
				TextNode(" and another ![second link](https://i.imgur.com)", TextType.TEXT),
			],
			new_nodes,
		)
	
	def test_beginning_end_links(self):
		node = TextNode(
		"[link](https://i.imgur.com) and another [second link](https://i.imgur.com)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
						"second link", TextType.LINK, "https://i.imgur.com"
				),
			],
			new_nodes,
		)
	
	def test_multiple_together_links(self):
		node = TextNode(
		"Links: [link](https://i.imgur.com)[second link](https://i.imgur.com)[link](https://i.imgur.com)",
		TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("Links: ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
				TextNode(
						"second link", TextType.LINK, "https://i.imgur.com"
				),
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
			],
			new_nodes,
		)
	
	def test_split_not_text_links(self):
		nodes = [
			TextNode("This is code", TextType.CODE),
			TextNode("This is bold", TextType.BOLD),
			TextNode("This is italic", TextType.ITALIC),
			TextNode("This is text and an [link](https://i.imgur.com)", TextType.TEXT),
			TextNode("This is link", TextType.LINK, "https://boot.dev"),
			TextNode("This is link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
		]
		new_nodes = split_nodes_link(nodes)
		self.assertListEqual(
			[
				TextNode("This is code", TextType.CODE),
				TextNode("This is bold", TextType.BOLD),
				TextNode("This is italic", TextType.ITALIC),
				TextNode("This is text and an ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://i.imgur.com"),
				TextNode("This is link", TextType.LINK, "https://boot.dev"),
				TextNode("This is link", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes
		)