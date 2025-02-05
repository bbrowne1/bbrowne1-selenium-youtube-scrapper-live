
# YouTube Trending Videos Scraper

This Python script scrapes the top 10 trending videos from YouTube and saves the data to a CSV file. The script uses Selenium to automate the web scraping process and Pandas to handle the data.

## Features

- **Automated Web Scraping**: Uses Selenium to navigate and extract data from YouTube's trending page.
- **Headless Browser**: Runs in a headless Chrome browser, making it efficient and suitable for server environments.
- **Data Extraction**: Extracts video title, URL, thumbnail URL, channel name, and description.
- **CSV Export**: Saves the extracted data to a CSV file for further analysis.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium
- Pandas
- ChromeDriver

You can install the required Python packages using pip:

```bash
pip install selenium pandas
```

Additionally, download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and ensure it is in your system's PATH.

## Usage

1. Clone the repository or download the script.

2. Run the script using Python:

```bash
python scraper.py
```

3. The script will output the scraped data to the console and save it to a file named `trending.csv`.

## Output

The script generates a CSV file (`trending.csv`) with the following columns:

- **title**: The title of the video.
- **url**: The URL of the video.
- **thumbnail_url**: The URL of the video's thumbnail image.
- **channel**: The name of the channel that uploaded the video.
- **description**: A brief description of the video.

## Example Output

```csv
title,url,thumbnail_url,channel,description
"Video Title 1","https://www.youtube.com/watch?v=example1","https://i.ytimg.com/vi/example1/default.jpg","Channel Name 1","Description of Video 1"
"Video Title 2","https://www.youtube.com/watch?v=example2","https://i.ytimg.com/vi/example2/default.jpg","Channel Name 2","Description of Video 2"
...
```

## Notes

- The script is configured to run in a headless mode, which means it does not open a browser window. If you want to see the browser in action, you can remove the `--headless` argument from the `chrome_options`.
- Ensure that the ChromeDriver version matches your installed version of Chrome.
- The script currently scrapes the top 10 trending videos. You can modify the script to scrape more videos by adjusting the slice in the list comprehension (`videos[:10]`).

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further to better suit your project's needs!
