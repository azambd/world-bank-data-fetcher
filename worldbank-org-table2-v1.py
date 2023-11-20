import requests
import csv

def make_post_request(url, payload, headers):
    """
    Make a POST request to a given URL with the specified payload and headers.

    Parameters:
    url (str): The URL to which the request is sent.
    payload (dict): The payload for the POST request.
    headers (dict): The headers for the POST request.

    Returns:
    dict: The JSON response received from the server.
    """
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

def parse_data(json_data):
    """
    Parse JSON data to extract relevant fields.

    Parameters:
    json_data (dict): The JSON data containing the fiscal data.

    Returns:
    list: List of extracted data.
    """
    parsed_data = []
    for row in json_data['rows']:
        fiscal_year = row['columns'][0]['data']
        country = row['columns'][1]['data']
        financier = row['columns'][2]['data']
        parsed_data.append([fiscal_year, country, financier])
    return parsed_data

def fetch_and_parse_data(url, headers, pages):
    """
    Fetch and parse data from multiple pages.

    Parameters:
    url (str): The URL to which the request is sent.
    headers (dict): The headers for the POST request.
    pages (int): Number of pages to fetch.

    Returns:
    list: Consolidated data from all pages.
    """
    all_data = []
    for page in range(1, pages + 1):
        print(f"Now crawling page: {page}")
        payload = {
            "report_id": "ibrd_ida_netprojects",
            "csrfmiddlewaretoken": None,
            "filters": {"page": page},
            "counttype": "10"
        }
        response_data = make_post_request(url, payload, headers)
        page_data = parse_data(response_data)
        all_data.extend(page_data)
    return all_data

# URL and headers for the POST request
url = "https://financesapp.worldbank.org/providers/get-report-data/"

headers = {
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'https://financesapp.worldbank.org/summaries/ibrd-ida/',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Linux"',
    # Note: Cookies are typically session-specific and may need to be updated or omitted
}

# Fetch and parse data for pages 1 to 10
try:
    consolidated_data = fetch_and_parse_data(url, headers, 10)

    # CSV file path
    csv_file_path = 'world_bank_data_pages_1_10.csv'

    # Writing data to CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Fiscal Year', 'Country', 'Financier'])
        writer.writerows(consolidated_data)

    print(f"Data successfully written to {csv_file_path}")
except Exception as e:
    print(f"Error: {e}")
