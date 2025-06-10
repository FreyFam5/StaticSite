import unittest
from markdown_to_blocks import BlockType, block_to_block_type


## Test Variables
header = "# Header"
code = "```\nCode\n```"
quote = """
> A
> Quote
> Here
"""
unordered_list = """
- List Item
- List Item Two
- List Item Too
"""
ordered_list = """
1. List Item One
2. List Item Two
3. List Item Three
"""
paragraph = "Hello There!"


class TestBlockType(unittest.TestCase):
	def test_block_type(self):
		block_types = [
			block_to_block_type(header),
			block_to_block_type(code),
			block_to_block_type(quote),
			block_to_block_type(unordered_list),
			block_to_block_type(ordered_list),
			block_to_block_type(paragraph),
			block_to_block_type("")
		]

		self.assertListEqual(
			block_types, 
			[
				BlockType.HEADING,
				BlockType.CODE,
				BlockType.QUOTE,
				BlockType.UNORDERED_LIST,
				BlockType.ORDERED_LIST,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH
			]
		)
	
	def test_heading_hash_amount(self):
		block_types = [
			block_to_block_type(header),
			block_to_block_type(f"#{header}"),
			block_to_block_type(f"##{header}"),
			block_to_block_type(f"###{header}"),
			block_to_block_type(f"####{header}"),
			block_to_block_type(f"#####{header}"),
			block_to_block_type(f"######{header}"),
		]
		self.assertListEqual(
			block_types,
			[
				BlockType.HEADING,
				BlockType.HEADING,
				BlockType.HEADING,
				BlockType.HEADING,
				BlockType.HEADING,
				BlockType.HEADING,
				BlockType.PARAGRAPH
			]
		)
	
	def test_code_backtick_amount(self):
		block_types = [
			block_to_block_type(code),
			block_to_block_type(f"`{code}`"),
			block_to_block_type(f"``{code}``"),
			block_to_block_type(f"`{code}``"),
			block_to_block_type("```"),
			block_to_block_type("``````"),
		]
		self.assertListEqual(
			block_types,
			[
				BlockType.CODE,
				BlockType.CODE,
				BlockType.CODE,
				BlockType.CODE,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH,
			]
		)
	
	def test_quote(self):
		block_types = [
			block_to_block_type(quote),
			block_to_block_type(f"{quote}\n >Item 4"), # Starts with space
			block_to_block_type(f"{quote}\n- Item 4"), # Starts with not a quote
			block_to_block_type(f"{quote}\nItem 4"), # No Quote
		]
		self.assertListEqual(
			block_types,
			[
				BlockType.QUOTE,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH
			]
		)
	
	def test_unordered_list(self):
		block_types = [
			block_to_block_type(unordered_list),
			block_to_block_type(f"{unordered_list}\n - Item 4"), # Starts with space
			block_to_block_type(f"{unordered_list}\n>Item 4"), # Starts with not a unordered_list
			block_to_block_type(f"{unordered_list}\nItem 4"), # No Unordered_list
		]
		self.assertListEqual(
			block_types,
			[
				BlockType.UNORDERED_LIST,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH
			]
		)

	def test_ordered_list(self):
		block_types = [
			block_to_block_type(ordered_list),
			block_to_block_type(f"{ordered_list}\n 4. Item 4"), # Starts with space
			block_to_block_type(f"{ordered_list}\n>Item 4"), # Starts with not a ordered_list
			block_to_block_type(f"{ordered_list}\nItem 4"), # No ordered_list
			block_to_block_type(f"{ordered_list}\n5. Item 4"), # Misordered List
		]
		self.assertListEqual(
			block_types,
			[
				BlockType.ORDERED_LIST,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH,
				BlockType.PARAGRAPH
			]
		)