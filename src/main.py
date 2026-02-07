import os
import shutil
from sys import argv

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
if len(argv) > 1:
    basepath = argv[1]
else:
    basepath = "/"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(
        dir_path_content="./content",
        template_path="./template.html",
        dest_dir_path="./docs",
        basepath=basepath
    )
    
main()
