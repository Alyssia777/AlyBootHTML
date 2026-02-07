import os
from markdown_blocks import markdown_to_html_node

def extract_title(content):
    #Extract title from content using the '# ' prefix, or raised an exception if no title is found.
    for line in content.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path} with basepath {basepath}")
    with open(from_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html_string = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, dir_path_content)
                dest_path = os.path.join(dest_dir_path, relative_path)
                dest_path = dest_path[:-3] + '.html'  # Change .md to .html
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(from_path, template_path, dest_path, basepath)