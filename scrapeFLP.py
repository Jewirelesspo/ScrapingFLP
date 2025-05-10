import requests
import markdownify
import urllib3 # Added import for urllib3 to suppress warnings

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_and_convert_to_markdown(url, output_filename):
    try:
        # Fetch HTML content
        response = requests.get(url, verify=False) # Added verify=False
        response.raise_for_status()  # Raise an exception for HTTP errors
        # Explicitly decode the content as UTF-8
        html_content = response.content.decode('utf-8')

        # Convert HTML to Markdown
        markdown_content = markdownify.markdownify(html_content, heading_style='atx')

        # Save to Markdown file
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully converted {url} to {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    base_url = "https://www.feynmanlectures.caltech.edu/III_{lecture_num}.html"
    output_base_filename = "feynman_lecture_III_{lecture_num}.md"

    for i in range(1, 22):  # Loop from 1 to 21
        lecture_number_str = f"{i:02d}"  # Format number to two digits (e.g., 01, 02, ..., 21)
        lecture_url = base_url.format(lecture_num=lecture_number_str)
        output_md_file = output_base_filename.format(lecture_num=lecture_number_str)
        
        print(f"Processing {lecture_url} -> {output_md_file}")
        scrape_and_convert_to_markdown(lecture_url, output_md_file)
