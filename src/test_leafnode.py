import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	
	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Boot Dev Link", {"href": "https://boot.dev"})
		self.assertEqual(node.to_html(), '<a href="https://boot.dev">Boot Dev Link</a>')
	
	def test_leaf_no_value(self):
		try:
			node = LeafNode("p")
		except ValueError as e:
			self.assertRaises(e)
	
	def test_leaf_no_tag(self):
		node = LeafNode(None, "This is text")
		self.assertEqual("This is text", node.to_html())