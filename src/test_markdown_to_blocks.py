import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
				blocks,
				[
						"This is **bolded** paragraph",
						"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
						"- This is a list\n- with items",
				],
		)
	
	def test_markdown_to_blocks_word(self):
		md = """


Word



"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
				blocks,
				[
						"Word"
				],
		)

	def test_markdown_to_blocks_no_words(self):
		md = """






"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
				blocks,
				[],
		)

	def test_markdown_to_blocks_single_line(self):
		md = """A line"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
				blocks,
				["A line"],
		)