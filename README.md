# Markdown to HTML Converter

Application to convert Markdown text to HTML tags.

## Overview

Markdown is a lightweight markup language with plain-text formatting syntax. This project provides functionality to convert Markdown files to HTML files, preserving the basic Markdown syntax for the features listed below.

## Features

- Convert Markdown files to HTML files.
- Supports conversion of headings(H1 to H6), unformatted text, links(in header, unformatted text(single or multiple lines)) and blank lines.

## Assumptions

- Any non heading or blank line is considered to be unformatted text.
- When a standalone link is provided in a line, the code follows the same syntax as [online converter](https://markdowntohtml.com) and considers that an unformatted text and a link.
- For link processing, when an invalid link is supplied, the entire text is treated as an unformatted text.
- Unnecessary blank lines are removed to keep the generated html file readable.

## Installation

No installation required. Simply include the `MarkdownConverter` class in your Python project. A sample main.py has been implemented to highlight this.

## Usage of the converter class

```python
from markdown_converter import MarkdownConverter

# Initialize MarkdownConverter instance
converter = MarkdownConverter()

# Convert Markdown to HTML
# Input file name is taken as command line input
converter.convert(input_file)
```

## Running the Program

To execute the program provide the input markdown file as a command line argument as follows.
```
python3 main.py test.md
```

The html file with the same name will be generated in the same folder after successful execution of the application.

## Tests

### Prerequisites

Before running the tests, make sure you have installed pytest. You can install it using pip:

```
pip install pytest
```

### Running Tests

Tests are collated in file `test_markdown_converter.py` and can be executed using the command:

```
pytest
```

### Code Coverage

To display code coverage execute the below commands:
```
python3 -m pip install coverage
```
```
coverage run -m pytest
coverage report -m
```

## Future Work

1. Add additional markdown syntaxes like - ordered and unordered lists, images, formatting etc.
2. Implement stream processing for large markdown files.
