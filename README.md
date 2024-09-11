# Web Crawler Project README

## Overview

This web crawler project is designed to extract and organize data from websites. It uses various techniques to gather information such as HTML content, links, images, and contact details. The project aims to provide a comprehensive overview of a given website, including its structure, content, and metadata.

## Features

- Extracts HTML content from websites
- Identifies and categorizes links (external, social media, directories)
- Takes screenshots of websites
- Saves images from the site
- Finds and extracts email addresses and phone numbers
- Provides DNS information
- Allows for recursive crawling of subdirectories

## Key Components

### ParentDir Class

The `ParentDir` class serves as the foundation for the web crawler. It takes two inputs:
- URL: The starting URL of the website to be crawled
- Directory: An optional parameter for specifying a particular directory within the website

### Main Functions

1. `callurl()`: Downloads the HTML source code of the input website
2. `findinglinks()`: Identifies and categorizes links in the source code
3. `screenshot()`: Captures a screenshot of the provided site using Selenium
4. `saveimage()`: Saves images from the site in a designated folder
5. `contact()`: Finds and prints all the emails and phone numbers
6. `output()`: Prints all the values collected by the functions
7. `finddir()`: Downloads the HTML source code of the requested directory
8. `dns_info()`: Provides DNS-related information
9. `giveback()`: Returns the directories present in the current level

## Usage

1. Run the main script
2. Enter the starting website URL when prompted
3. Choose options for the type of information you want to extract (description, links, directories, screenshot, images, social media handles)
4. Enter the depth for recursive crawling (number of levels to crawl subdirectories)
5. The crawler will process the site according to your inputs
6. Review the extracted data and choose another directory to continue crawling if desired

## Dependencies

- Python
- Selenium
- Requests
- BeautifulSoup
- re (regular expressions)
- dns.resolver

## Installation

1. Install Python if not already installed
2. Install required dependencies:
   ```
   pip install selenium requests beautifulsoup4 dnspython
   ```

## Configuration

Ensure that your system meets the requirements for running Selenium. You may need to install a WebDriver (e.g., ChromeDriver) depending on your operating system and preferred browser.

## Limitations

- May not work correctly with dynamic or heavily JavaScript-dependent sites
- Could potentially overwhelm servers with excessive requests
- Not designed for large-scale production use; intended for educational and small-scale projects

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or issues.

## License

[Insert license information here]

## Acknowledgments

This project was inspired by various web scraping tutorials and examples available online. Special thanks to the creators of the libraries used in this project for their contributions to the Python ecosystem.

## Screenshots

Here are some screenshots of the project in action:

<img src="images/links.png" alt="Links from the site" height="500">
<img src="images/screen1.png" alt="Screenshot of the site" height="500">
<img src="images/image0.png" alt="An image saved from the site" height="400">
<img src="images/output.png" alt="User output" height="200">

These images demonstrate the key features of the web crawler, including link extraction, screenshot capture, image saving, and the final output display. They provide visual representations of the project's capabilities and can help users understand how the tool works.