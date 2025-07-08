from enum import Enum
import re

def block_to_block_type(block):
    lines = block.splitlines()
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(re.match(r"^>", line) for line in lines):
        return BlockType.QUOTE
    elif all(re.match(r"^\- ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    elif all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
