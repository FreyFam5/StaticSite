import os
import shutil


def copy_paste(path_from, path_to):
		if os.path.isfile(path_from):
			shutil.copy(path_from, path_to)
			print(f"{path_from} -> {path_to}")
		else:
			path_list = os.listdir(path_from)
			os.mkdir(path_to)
			for path in path_list:
				copy_paste(f"{path_from}/{path}", f"{path_to}/{path}")