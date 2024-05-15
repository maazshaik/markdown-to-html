import pytest
from to_html import MarkdownConverter

@pytest.fixture
def converter():
    '''Returns a MarkdownConverter instance with no input file'''
    return MarkdownConverter()

# Test is_heading method
@pytest.mark.parametrize("markdown_text, expected_html", [
    # Test Case 1: Heading 1
    ("# Heading 1", True),
    # Test Case 2: Heading 2
    ("## Heading 2", True),
    # Test Case 3: Invalid heading (more than h6)
    ("####### Invalid Heading", False),
    # Test Case 4: Invalid heading (invalid format)
    ("#Not a heading", False),
    # Test Case 5: Not a heading
    ("Not a heading", False),
    # Test Case 6: Blank Line
    ("", False)
])
def test_is_heading(converter,markdown_text, expected_html):
    assert converter.is_heading(markdown_text) == expected_html

# Test convert_heading method
@pytest.mark.parametrize("markdown_text, expected_html", [
    ('# Heading 1', '<h1>Heading 1</h1>'), 
    ('## Heading 2', '<h2>Heading 2</h2>'), 
    ('### Heading 3', '<h3>Heading 3</h3>'), 
    ('#### Heading 4', '<h4>Heading 4</h4>'),
    ('##### Heading 5', '<h5>Heading 5</h5>'), 
    ('###### Heading 6', '<h6>Heading 6</h6>'),
])
def test_convert_heading(converter, markdown_text, expected_html):
    if converter.is_heading(markdown_text):
        assert converter.convert_heading(markdown_text) == expected_html

# Test convert_link method
@pytest.mark.parametrize("markdown_text, expected_html", [
    # Test Case 1: Valid link
    ('[Link text](https://www.example.com)', '<a href="https://www.example.com">Link text</a>'),
    # Test Case 2: Invalid link
    ('[Link text(https://www.example.com)', '[Link text(https://www.example.com)'),
    # Test Case 3: Link with unformatted text
    ('This is a paragraph [with an inline link](http://google.com). Neat, eh?', 'This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?'),
    # Test Case 4: Link with header
    ('## This is a header [with a link](http://yahoo.com)', '## This is a header <a href="http://yahoo.com">with a link</a>'),
    # Test Case 5: Not a link
    ('There is not link in this line', 'There is not link in this line')
])
def test_convert_link(converter, markdown_text, expected_html):
    assert converter.convert_link(markdown_text) == expected_html

# Test convert_unformatted method
@pytest.mark.parametrize("markdown_text, expected", [
    # Test Case 1: Simple unformatted
    ('This is a paragraph.', '<p>This is a paragraph.</p>'),
    # Test Case 2: Unformatted with link
    ('This is a paragraph [with an inline link](http://google.com). Neat, eh?', '<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>'),
    # Test Case 3: Only link
    ('[with an inline link](http://google.com)', '<p><a href="http://google.com">with an inline link</a></p>'),
])
def test_convert_unformatted(converter, markdown_text, expected):
    assert converter.convert_unformatted(markdown_text) == expected

# Integration Test
# Test process_lines method
@pytest.mark.parametrize("markdown_lines, expected_html", [
    # Test Case 1: Single heading line
    (['# Heading 1'], ['<h1>Heading 1</h1>', '']),
    # Test Case 2: Multiple heading lines
    (['# Heading 1', '## Heading 2'], ['<h1>Heading 1</h1>', '', '<h2>Heading 2</h2>', '']),
    # Test Case 3: Single unformatted line
    (['This is a paragraph.'], ['<p>This is a paragraph.</p>']),
    # Test Case 4: Multiple unformatted lines
    (['How are you?\n', 'Whats going on?\n', 'Hello World'], ['<p>How are you?\nWhats going on?\nHello World</p>']),
    # Test Case 5: Mixture of heading and unformatted lines
    (['# Heading 1', 'This is a paragraph.', '', '## Heading 2', 'Hello World'], 
     ['<h1>Heading 1</h1>', '', '<p>This is a paragraph.</p>', '', '<h2>Heading 2</h2>', '', '<p>Hello World</p>']),
    # Test Case 6: Additional Blank lines
    (['', '# Heading 1', '', 'This is a paragraph.', ''], 
     ['<h1>Heading 1</h1>', '', '<p>This is a paragraph.</p>', ''])
])
def test_process_lines(converter, markdown_lines, expected_html):
    assert converter.process_lines(markdown_lines) == expected_html
