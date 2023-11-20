import requests
import csv
import re

def fetch_worldbank_data(page, counttype="10"):
    """
    Fetches data from the World Bank API for a specific page.
    Args:
    - page: The page number to fetch data from.
    - counttype: Count type for the API call (default is "10").

    Returns:
    - JSON response from the API if successful, or an error message if not.
    """
    url = "https://financesapp.worldbank.org/providers/get-report-data/"
    payload = {
        "report_id": "ibrd_ida_projects",
        "csrfmiddlewaretoken": None,
        "filters": {"page": page},
        "counttype": counttype
    }
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://financesapp.worldbank.org/summaries/ibrd-ida/',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Linux"',
    }

    with requests.Session() as session:
        response = session.post(url, json=payload, headers=headers)
        return response.json() if response.status_code == 200 else {"error": "Request failed with status code {}".format(response.status_code)}

def parse_worldbank_data(response_data):
    """
    Parses the World Bank API response data and extracts project information.
    Args:
    - response_data: The JSON data received from the World Bank API.

    Returns:
    - Path to the CSV file where the data is saved.
    """
    def extract_project_info(rows, index):
        if len(rows[index]['columns']) == 7:
            link_name_data = rows[index - 1]['columns'][0]['data']
            link_search = re.search(r'href="([^"]+)"', link_name_data)
            link = link_search.group(1) if link_search else "No Link"
            name = re.sub(r'<[^>]+>', '', link_name_data).strip()
            country = rows[index]['columns'][4]['data']
            status = rows[index]['columns'][5]['data']
            approval_date = rows[index]['columns'][6]['data']
            return [name, link, country, status, approval_date]
        return None

    csv_rows = [extract_project_info(response_data['rows'], i) for i in range(len(response_data['rows'])) if extract_project_info(response_data['rows'], i)]
    csv_file_path = 'world_bank_projects.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Project Name', 'Project Link', 'Country', 'Status', 'Approval Date'])
        writer.writerows(filter(None, csv_rows))
    return csv_file_path


# Main process to fetch and parse data from pages 1 to 10
all_data_rows = []
for page in range(1, 4):
    print(f"Now crawling Page: {page}")
    api_data = fetch_worldbank_data(page)
    if 'error' not in api_data and 'rows' in api_data:
        all_data_rows.extend(api_data['rows'])

if all_data_rows:
    combined_data = {'rows': all_data_rows}
    csv_file_path = parse_worldbank_data(combined_data)
    print(f"Data from pages 1 to 3 has been written to CSV file at: {csv_file_path}")
else:
    print("No data fetched or an error occurred.")
