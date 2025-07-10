import os
import shutil
import sys
from page_generator import generate_pages_recursive, generate_page

def delete_dir(destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)

def copy_dir(destination_path, source_path):
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    if os.path.exists(destination_path) and os.path.exists(source_path):
        if os.path.isfile(source_path):
            print(source_path)
            shutil.copy(source_path, destination_path)
        elif os.path.isdir(source_path):
            file_and_dir = os.listdir(source_path)
            for element in file_and_dir:
                if os.path.isfile(os.path.join(source_path, element)):
                    print(os.path.join(source_path, element))
                    shutil.copy(os.path.join(source_path, element), os.path.join(destination_path, element))
                elif os.path.isdir(os.path.join(source_path, element)):
                    if not os.path.exists(os.path.join(destination_path, element)):
                        os.mkdir(os.path.join(destination_path, element))
                    copy_dir(os.path.join(destination_path, element), os.path.join(source_path, element))



def main():
    if len(sys.argv) == 1:
        base_path = "/"
    else:
        base_path = sys.argv[1]
    public_path = "/home/mattls/workspace/github.com/mattls95/static-site-generator/docs"
    static_path = "/home/mattls/workspace/github.com/mattls95/static-site-generator/static"
    delete_dir(public_path)
    copy_dir(public_path, static_path)
    generate_pages_recursive(base_path=base_path)

main()
