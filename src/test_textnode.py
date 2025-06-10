import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_not_eq_text(self):
		node = TextNode("This is a node", TextType.ITALIC)
		node2 = TextNode("This is also a node", TextType.ITALIC)
		self.assertNotEqual(node, node2)

	def test_not_eq_type(self):
		node = TextNode("This is a node", TextType.ITALIC)
		node2 = TextNode("This is a node", TextType.TEXT)
		self.assertNotEqual(node, node2)

	def test_not_eq_url(self):
		node = TextNode("This is a node", TextType.CODE, "https://boot.dev")
		node2 = TextNode("This is a node", TextType.CODE)
		self.assertNotEqual(node, node2)

	def test_not_eq_url_text(self):
		node = TextNode("This is a node", TextType.IMAGE, "https://boot.dev")
		node2 = TextNode("This is a node", TextType.IMAGE, "https://image.png")
		self.assertNotEqual(node, node2)

	## Testing text node to html
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
	
	def test_bold(self):
		node = TextNode("Bold Text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "Bold Text")

	def test_italic(self):
		node = TextNode("italic Text", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "italic Text")
	
	def test_code(self):
		node = TextNode("Code Text", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "Code Text")
	
	def test_link(self):
		node = TextNode("Link Text", TextType.LINK, "https://boot.dev")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "Link Text")
		self.assertEqual(html_node.props_to_html(), 'href="https://boot.dev"')

	def test_image(self):
		node = TextNode("Image Text", TextType.IMAGE, "https://boot.dev")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props_to_html(), 'src="https://boot.dev" alt="Image Text"')


if __name__ == "__main__":
	unittest.main()