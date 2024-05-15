import re

class MarkdownConverter:
    """
    A class used to convert a file containing markdown text to html tags
    """
    def __init__(self):
        pass 
    
    def convert(self, input_file="default.md"):
        """
        Processes a file containing markdown text and generates a file with the html equivalent
        Parameters
        ----------
        input_file : str
            Markdown file name to be converted
        """
        with open(input_file, 'r') as f:
            markdown_lines = f.readlines()

        html_lines = self.process_lines(markdown_lines)

        output_file = input_file.replace('.md', '.html')
        with open(output_file, 'w') as f:
            f.write('\n'.join(html_lines))

        print(f"HTML file '{output_file}' generated successfully.")

    def process_lines(self, markdown_lines):
        """
        Process markdown text and convert to html, line by line
        Parameters
        ----------
        markdown_lines : list[str]
            markdown text to be processed
        Returns
        ----------
        html_lines : list[str]
            Returns html text
        """
        html_lines = []
        buffer = []

        for line in markdown_lines:
            # Heading, append processed sections to output
            if self.is_heading(line):
                html_lines.append(self.convert_heading(line))
                html_lines.append('') 
            # Blank Line, append processed sections to output
            elif not line.strip():
                if buffer:
                    html_lines.append(self.convert_unformatted(''.join(buffer)))
                    html_lines.append('')
                    buffer.clear()
            else:  # Unformatted text continues
                buffer.append(line)

        # Convert any remaining buffered lines to a paragraph
        if buffer:
            html_lines.append(self.convert_unformatted(''.join(buffer)))
        
        return html_lines

    def is_heading(self, markdown_line):
        """
        Checks if the line inputed is a heading
        Parameters
        ----------
        markdown_line : str
            markdown text to be checked
        Returns
        ----------
        result : boolean
            Returns true if heading and false otherwise
        """
        words = markdown_line.split(' ')
        if words[0].startswith('#'):
            if  all(c == '#' for c in words[0]) and len(words[0]) < 7:
                return True
        return False
    
    def convert_heading(self, markdown_line):
        """
        Converts a heading in markdown to html
        Parameters
        ----------
        markdown_line : str
            markdown text to be converted
        Returns
        ----------
        html_text : str
            Returns the equivalent html conversion
        """
        split_line = markdown_line.split(' ')
        heading_level = split_line[0].count('#')
        # Separate heading text from #
        heading_text = ' '.join(split_line[1:]).strip()
        heading_with_links=self.convert_link(heading_text)
        html_text = f'<h{heading_level}>{heading_with_links}</h{heading_level}>'
        return html_text
    
    def convert_unformatted(self, markdown_unformatted):
        """
        Converts unformatted text in markdown to html
        Parameters
        ----------
        markdown_line : str
            markdown text to be converted
        Returns
        ----------
        html_text : str
            Returns the equivalent html conversion
        """
        unformatted_with_links=self.convert_link(markdown_unformatted)
        html_text = f'<p>{unformatted_with_links.strip()}</p>'
        return html_text

    def convert_link(self, markdown_link):
        """
        Converts a link in markdown to html (embedded within heading, unformatted_text or standalone)
        Parameters
        ----------
        markdown_line : str
            markdown text to be converted
        Returns
        ----------
        html_text : str
            Returns the equivalent html conversion
        """
        # Regex pattern to identify a link in a text
        link_pattern = r'\[([^]]+)]\(([^)]+)\)'
        html_text = re.sub(link_pattern, r'<a href="\2">\1</a>', markdown_link)
        # 2 is the url and 1 is the markdown text
        return html_text