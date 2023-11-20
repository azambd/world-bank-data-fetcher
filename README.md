
# World Bank Data Fetcher

This repository contains a Python script that efficiently fetches and processes project data from the World Bank API. The primary goal of this project is to provide an automated means to retrieve, parse, and store important project data in a structured format (CSV), making it easily accessible for further analysis or reporting. This script is particularly useful for data analysts and researchers focusing on global development projects.

## Main Features

- **Data Fetching Across Pages**: Automates the retrieval of data from multiple pages (1 to 10) of the World Bank API, ensuring comprehensive coverage of available project data.
- **Data Parsing**: Extracts key details from the API's response, including project names, URLs, countries, statuses, and approval dates.
- **CSV File Generation**: Organizes and stores the parsed data in a CSV file, facilitating easy access and further data manipulation.

## Requirements

This script requires Python 3.x and utilizes the following libraries:

- `requests`: Handles HTTP requests to the World Bank API.
- `csv`: Manages the creation and writing of CSV files.
- `re`: Processes regular expressions for data extraction.

## Installation

Clone the repository using:

```bash
git clone https://github.com/your-github-username/worldbank-data-fetcher.git
```

Navigate to the directory:

```bash
cd worldbank-data-fetcher
```

## Usage

Execute the script with Python:

```bash
python worldbank-org-table1-v1.py
```
A CSV file named `world_bank_projects.csv` will be generated, containing the structured project data.

```bash
python worldbank-org-table2-v1.py
```
A CSV file named `world_bank_data_pages_1_10.csv` will be generated, containing the structured project data.

## Functions Description

- `fetch_worldbank_data(page, counttype="10")`: Fetches data from a specific page of the World Bank API. It constructs the request with necessary headers and payload, handles the response, and returns the data in JSON format.

- `parse_worldbank_data(response_data)`: Parses the JSON response from the API. It extracts relevant project information from each row of data, including the project name, URL, country, status, and approval date. This function ensures the data is correctly formatted for CSV output.

## Contributing

Contributions to enhance or expand the functionalities of this script are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

Your Name - [azam@wscraper.com]

Project Link: https://github.com/your-github-username/worldbank-data-fetcher

## Acknowledgements

- [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information)
```

This revised `README.md` provides a clear overview of the project's purpose, its features, detailed descriptions of its functions, and instructions for installation, usage, and contribution. It also includes sections for licensing, contact information, and acknowledgements. 
