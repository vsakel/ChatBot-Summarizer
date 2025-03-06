import pymupdf4llm

# we parse the file into markdown because markdown preserves the structure and links of the original document.

def parse_file(file_path):
    parsed_file = pymupdf4llm.to_markdown(file_path, show_progress=False)
    return parsed_file
