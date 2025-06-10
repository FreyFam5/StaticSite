import functools
from markdown_to_blocks import *


class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props == None:
			return "None"
		return functools.reduce(lambda accum, key: accum + f'{key}="{self.props[key]}" ', self.props, '').strip()
	
	def __repr__(self):
		return f"HTML Node({self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, None, props)
	
	def to_html(self):
		if self.value == None:
			raise ValueError("Leaf nodes require a value!")
		if self.tag == None:
			return self.value
		return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>".replace(" None", "")


class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None):
		super().__init__(tag, None, children, props)
	
	def to_html(self):
		if self.tag == None:
			raise ValueError("Needs a tag to function")
		if self.children == None:
			raise ValueError("Needs children to function")
		
		base_string = ""
		for child in self.children:
			base_string += child.to_html()
			
		return f"<{self.tag}>{base_string}</{self.tag}>"