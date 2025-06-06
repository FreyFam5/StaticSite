import unittest
from htmlnode import HTMLNode


test_dict = {
		"href": "https://www.google.com",
		"target": "_blank",
}


class TestHTMLNode(unittest.TestCase):
	def test_props_to_html_equal(self):
		node = HTMLNode("<a>", "Link", None, test_dict)
		self.assertEqual('href="https://www.google.com" target="_blank"', node.props_to_html())
	
	def test_props_to_html_not_equal(self):
		node = HTMLNode("<a>", "Link", None, test_dict)
		node2 = HTMLNode("<a>", "Link")
		self.assertNotEqual(node, node2)
	
	def test_props_str(self):
		node = HTMLNode("<a>", "link", None, {"href": "https://boot.dev"})
		self.assertEqual(node.props_to_html(), 'href="https://boot.dev"')