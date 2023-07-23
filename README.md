# lightshot-bookmarks-downloader

## Project Description
A script for downloading lightshot screenshots from a google chrome bookmarks file named "bookmarks.html". The script specifically targets URLs that match the pattern `http://prntscr.com/[a-zA-z0-9]+` or `http://prnt.sc/[a-zA-z0-9]+`. After identifying these URLs, it proceeds to fetch and download images available at these locations.

## Dependencies
To run this script, you need to have the following Python libraries installed:

- requests_html
- beautifulsoup4 (bs4)
- nest_asyncio

## How to Run
Before running the script, make sure you have a file named "bookmarks.html" in the same directory as the script. This file should contain the URLs to scrape.

Run `main.py` to start the script. The script will create a folder named "pictures" in the same directory as the script. All downloaded images will be saved in this folder and named "1.png/jpg", "2..." and so on.