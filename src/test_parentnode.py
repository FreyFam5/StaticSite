import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
				parent_node.to_html(),
				"<div><span><b>grandchild</b></span></div>",
		)
	
	def test_to_html_no_children(self):
		parent_node = ParentNode("div", [])
		self.assertEqual(parent_node.to_html(), "<div></div>")
	
	def test_to_html_multiple_children(self):
		children_nodes = [
			LeafNode("p", "This is child one"),
			LeafNode("a", "This is child two", {"href": "https://boot.dev", "target": "this place"}),
			LeafNode("p", "This is child three")
		]
		parent_node = ParentNode("div", children_nodes)
		self.assertEqual(parent_node.to_html(), '<div><p>This is child one</p><a href="https://boot.dev" target="this place">This is child two</a><p>This is child three</p></div>')
	
	def test_to_html_nested_parents_and_multiple_children(self):
		children_nodes = [
			LeafNode("p", "This is child one"),
			LeafNode("a", "This is child two", {"href": "https://boot.dev", "target": "this place"}),
			LeafNode("p", "This is child three")
		]
		parent_node_one = ParentNode("div", children_nodes)
		parent_node_two = ParentNode("span", [LeafNode("p", "I'm all by myself")])
		leaf_node = LeafNode("p", "I'm at the top!")
		grandparent_node = ParentNode("html", [leaf_node, parent_node_one, parent_node_two])
		self.assertEqual(
			grandparent_node.to_html(), 
			"""<html><p>I'm at the top!</p><div><p>This is child one</p><a href="https://boot.dev" target="this place">This is child two</a><p>This is child three</p></div><span><p>I'm all by myself</p></span></html>""")
