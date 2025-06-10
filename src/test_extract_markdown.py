import unittest
from inline_markdown import *

class TestExtractMarkdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
				"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
	
	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
				"This is text with an [link](https://boot.dev)"
		)
		self.assertListEqual([("link", "https://boot.dev")], matches)
	
	def test_incorrect_syntax_images(self):
		matches = extract_markdown_images(
				"This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([], matches)
	
	def test_multiple_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and this is also an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([('image', 'https://i.imgur.com/zjjcJKZ.png'), ('image', 'https://i.imgur.com/zjjcJKZ.png')], matches)
	
	def test_incorrect_syntax_links(self):
		matches = extract_markdown_links(
				"This is text with an ![link](https://boot.dev)"
		)
		self.assertListEqual([], matches)
	
	def test_multiple_links(self):
		matches = extract_markdown_links(
			"This is text with an [link](https://bott.dev) and this is also an [link](https://bott.dev)"
		)
		self.assertListEqual([('link', 'https://bott.dev'), ('link', 'https://bott.dev')], matches)