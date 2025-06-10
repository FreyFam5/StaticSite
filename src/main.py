import os
import shutil
from generate_page import generate_pages_recursive
from copystatic import copy_paste


path_from = "./static"
path_to = "./public"

def main():
	print("Deleting public directory...")
	if os.path.exists(path_to):
		shutil.rmtree(path_to)

	print("Copying static files to public directory...")
	copy_paste(path_from, path_to)

	print("Generating page...")
	generate_pages_recursive("./content", "./template.html", "./public")

main()