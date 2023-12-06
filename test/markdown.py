a = 'test'

markdown_content = f"""# My Markdown File

This is a sample Markdown file created using Python.

## {a} 1

Here is some text for the first section.

## Section 2

And here is some text for the second section.
"""

file_path = 'example2.md'

with open(file_path, 'w') as file:
    file.write(markdown_content)

print(f"Markdown file '{file_path}' created successfully.")
