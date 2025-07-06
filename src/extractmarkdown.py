import re


def extract_markdown_images(text):
    alt_url_list = []
    image_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for image in image_list:
        alt_url_list.append(image)
    return alt_url_list

def extract_markdown_links(text):
    anchor_url_list = []
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for link in links:
        anchor_url_list.append(link)
    return anchor_url_list
