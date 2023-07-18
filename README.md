# ForReal Rental Research RPA

## Description
The ForReal Rental Research RPA (Robotic Process Automation) tool is designed to scrape house listings from ForReal.com and automatically fill a Google Form with the scraped data. It aims to automate the process of gathering rental property information, saving time and effort for researchers or anyone looking for rental listings.

This tool utilizes web scraping techniques to extract relevant details such as property location, price, description, and other key information from ForReal.com. The extracted data is then populated into a Google Form, streamlining the process of collecting rental property data.

## Features
- Automated scraping of rental listings from ForReal.com
- Extraction of key details such as property location, price, description, and more
- Population of scraped data into a Google Form
- Streamlined and efficient rental property research process

## Requirements
- Python 3.x
- Selenium
- ChromeDriver
- Google Chrome Browser
- Google Form (to populate the scraped data)

## Installation and Setup
1. Clone the repository:
   ```shell
   git clone https://github.com/guccigamp/ForReal-Rental-Research-RPA.git
   ```
2. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```
3. Download and configure ChromeDriver:
- Download the appropriate ChromeDriver version compatible with your Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Extract the downloaded archive and copy the `chromedriver` executable to a location in your system's PATH.

4. Configure the Google Form:
- Set up a Google Form where you want to populate the scraped data.
- Note the input field names or IDs that correspond to the relevant data fields such as location, price, description, etc.

5. Configure the script:
- Open `config.py` and update the variables with the necessary information, that is your Google Form URL, ForReal URL, your browser headers.

6. Run the script:
```shell
python main.py
```

## Usage
- Upon running the script, the ForReal-Rental-Research-RPA tool will launch a Chrome browser and navigate to ForRent.com.
- It will scrape the rental listings, extract the desired details, and populate them into the configured Google Form.
- You can monitor the progress and view the results in the Google Form.

## Limitations
- This tool relies on the current structure and elements of ForRent.com. Any changes to the website's structure may require updates to the script.
- Web scraping may be subject to legal and ethical considerations. Ensure you comply with the terms of service of the website you are scraping and respect the data owner's rights and privacy.

## Contributing
Contributions to the ForReal Rental Research RPA tool are welcome. If you encounter any issues, have suggestions for improvements, or would like to contribute new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).







