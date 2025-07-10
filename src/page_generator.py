import os
from markdown_to_html_node import markdown_to_html_node
public_dir = "/home/mattls/workspace/github.com/mattls95/static-site-generator/public"
content_dir = "/home/mattls/workspace/github.com/mattls95/static-site-generator/content"
template_path = "/home/mattls/workspace/github.com/mattls95/static-site-generator/template.html"

def generate_pages_recursive(dir_path_content=content_dir, template_path=template_path, dest_dir_path=public_dir):
    directories = os.listdir(dir_path_content)
    for dir in directories:
        if os.path.isfile(os.path.join(dir_path_content, dir)) and dir.endswith(".md"):
            generate_page(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir).replace(".md", ".html"))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir))

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_from = ""
    with open(from_path) as file:
        markdown_from = file.read()
    
    markdown_template = ""
    with open(template_path) as file:
        markdown_template = file.read()

    from_markdown_html_node = markdown_to_html_node(markdown_from)
    
    title = extract_title(markdown_from)
    content = from_markdown_html_node.to_html()

    markdown_template = markdown_template.replace("{{ Title }}", title)
    markdown_template = markdown_template.replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
            file.write(markdown_template)

def extract_title(markdown):
    if len(markdown.split("\n")) > 1:
        lines = markdown.split("\n")
        for line in lines:
            clean_line = line.strip()
            if clean_line.startswith("#"):
                return clean_line[1:].strip()
    else:
        return markdown[1:].strip()
    raise Exception("no h1 header found")