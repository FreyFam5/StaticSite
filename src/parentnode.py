
from htmlnode import HTMLNode

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