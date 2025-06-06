import functools

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