import os
import sys
import shutil
from generate_page import generate_pages_recursive
from copystatic import copy_paste


path_from = "./static"
path_to = "./docs"


def main():
	basepath = "/"
	if len(sys.argv) > 1:
		basepath = sys.argv[1]

	print("Deleting public directory...")
	if os.path.exists(path_to):
		shutil.rmtree(path_to)

	print("Copying static files to public directory...")
	copy_paste(path_from, path_to)

	print("Generating page...")
	generate_pages_recursive("./content", "./template.html", path_to, basepath)

main()