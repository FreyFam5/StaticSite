import os
from pathlib import Path
from markdown_to_html import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for path in os.listdir(dir_path_content):
		path_from_name = f"{dir_path_content}/{path}"
		path_to_name = f"{dest_dir_path}/{path}"
		if os.path.isfile(path_from_name):
			path_to_name = Path(path_to_name).with_suffix(".html")
			generate_page(path_from_name, template_path, path_to_name)
		else:
			generate_pages_recursive(path_from_name, template_path, path_to_name)


def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	markdown_file = ""
	with open(from_path) as f:
		markdown_file = f.read()

	template_file = ""
	with open(template_path) as f:
		template_file = f.read()

	html_string = markdown_to_html_node(markdown_file).to_html()
	title = extract_title(markdown_file)
	new_file = template_file.replace("{{ Title }}", title, 1).replace("{{ Content }}", html_string, 1)

	dir_name = os.path.dirname(dest_path)
	if not os.path.isfile(dest_path) and not os.path.exists(dir_name):
		os.makedirs(dir_name)
	with open(dest_path, "w") as f:
		f.write(new_file)


def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			return line[2:]
	raise Exception("Excpected header (#...)")