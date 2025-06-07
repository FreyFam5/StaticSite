import re

## Uses regex to take out the image (![image alt text](https://i.imgur.com/zjjcJKZ.png))
def extract_markdown_images(text):
	return re.findall(r"!\[([^\[\]]*)\]\(([^\)\(]*)\)", text)

## Uses regex to take out the link ([link text](https://bott.dev))
def extract_markdown_links(text):
	return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\)\(]*)\)", text)