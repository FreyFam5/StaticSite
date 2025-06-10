from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "blockquote"
	UNORDERED_LIST = "unordered list"
	ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
	lines = markdown.split("\n\n")
	new_lines = []
	for line in lines:
		new_line = line.strip()
		if new_line == "":
			continue
		new_lines.append(new_line)
	return new_lines

def block_to_block_type(markdown):
	if markdown == "":
		return BlockType.PARAGRAPH
	if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING
	
	markdown_lines = markdown.split("\n")
	if markdown.startswith("```") and markdown.endswith("```") and len(markdown_lines) > 1:
		return BlockType.CODE
	
	quote = True
	unli = True
	orli_count = 1
	true_list_count = 1
	# Checks each line for its starting character for lists and quote blocks
	for line in markdown_lines:
		if line == "":
			continue
		true_list_count += 1
		if not line.startswith(">") and quote:
			quote = False
		if not line.startswith("- ") and unli:
			unli = False
		if line.startswith(f"{orli_count}. "):
			orli_count += 1
		
	if quote:
		return BlockType.QUOTE
	if unli:
		return BlockType.UNORDERED_LIST
	if orli_count == true_list_count:
		return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH
