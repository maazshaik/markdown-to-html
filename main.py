import argparse, os
from markdown_converter.to_html import MarkdownConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, help='Markdown file to be converted')
    args = parser.parse_args()
    input_file = args.input_file

    try:
        # Check if input file has .md extension
        if not input_file.endswith('.md'):
            raise ValueError

        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError
        
        mth = MarkdownConverter()
        mth.convert(args.input_file)

    except ValueError:
        print(f"Error: Input file must be a Markdown (.md) file.")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")