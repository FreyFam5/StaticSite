import unittest
from inline_markdown import *

class TestTextToTextNodes(unittest.TestCase):
	def test_texttotextnodes(self):
		text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		self.assertListEqual(
			text_to_textnodes(text),
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.TEXT),
				TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			]
		)
	
	def test_if_empty(self):
		self.assertListEqual([], text_to_textnodes(""))
	
	def test_nested_syntax(self):
		text = "This is **text _italic_** with an _italic `code block`_ word and a `code ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		output = text_to_textnodes(text)
		expected_output = [
			TextNode("This is ", TextType.TEXT), 
			TextNode("text _italic_", TextType.BOLD), 
			TextNode(" with an ", TextType.TEXT), 
			TextNode("italic `code block`", TextType.ITALIC), 
			TextNode(" word and a ", TextType.TEXT), 
			TextNode("code ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) block", TextType.CODE), 
			TextNode(" and an ", TextType.TEXT), 
			TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
			TextNode(" and a " , TextType.TEXT), 
			TextNode("link", TextType.LINK, "https://boot.dev")
		]
		self.assertListEqual(output, expected_output)

	def test_one_markdown(self):
		text = "This is **bold**"
		self.assertListEqual(
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("bold", TextType.BOLD)
			],
			text_to_textnodes(text)
		)
	
	def test_butting_markdown(self):
		text = "This is **bold**_italic_"
		self.assertListEqual(
			[
				TextNode("This is ", TextType.TEXT),
				TextNode("bold", TextType.BOLD),
				TextNode("italic", TextType.ITALIC),
			],
			text_to_textnodes(text)
		)
	
	def test_incrroect_nesting(self):
		text = "**bold _italic** still bold_"
		self.assertListEqual(
			[
				TextNode("bold _italic", TextType.BOLD),
				TextNode(" still bold", TextType.TEXT)
			],
			text_to_textnodes(text)
		)