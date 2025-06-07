from textnode import *
from splitnodes import *
from texttotextnodes import *

def main():
	text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
	print(text_to_textnodes(text))


main()