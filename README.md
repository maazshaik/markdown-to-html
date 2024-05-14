# Markdown to HTML Converter

Program to convert Markdown files to HTML.

## Overview

Markdown is a lightweight markup language with plain-text formatting syntax. This project provides functionality to convert Markdown files to HTML files, preserving the basic Markdown syntax for the features listed below.

## Features

- Convert Markdown files to HTML files.
- Supports conversion of headings(H1 to H6), unformatted text, links(in header, unformatted text(single or multiple lines)) and blank lines.

## Assumptions

- Any non heading or blank line is considered to be unformatted text
- When a standalone link is provided in a line, the code follows the same syntax as [online converter](https://markdowntohtml.com) and considers that an unformatted text and a link
- For link processing, when an invalid link is supplied, the entire text is treated as an unformatted text
- Unncessary Blank lines are removed to keep the generated html file readable

## Installation

No installation required. Simply include the `MarkdownConverter` class in your Python project. A sample main.py has been implemented to highlight this

## Usage

```python
from MarkdownConverter import MarkdownConverter

# Initialize MarkdownConverter with input Markdown file
converter = MarkdownConverter('input.md')

# Convert Markdown to HTML
converter.convert()
```

## Tests

### Prerequisites

Before running the tests, make sure you have installed pytest. You can install it using pip:

```pip install pytest```

### Running Tests

Tests are collated in file `test_markdown_converter` and can be executed using the command

```pytest```
