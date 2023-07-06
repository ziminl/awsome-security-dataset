import requests
from bs4 import BeautifulSoup

def scrape_xml_files(query):
    query = query.replace(' ', '+')
    for page in range(1, 51): ##51 = 50 page
        start_index = (page - 1) * 10
        url = f'https://www.google.com/search?q={query}&start={start_index}&num=10&as_filetype=xml'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        xml_links = soup.select('a[href$=".xml"]')

        for link in xml_links:
            file_url = link['href']
            file_name = link.text.strip()
            print(f'Downloading: {file_name}')
            download_file(file_url, file_name)

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'{filename} downloaded successfully!')

search_query = 'uaf'
scrape_xml_files(search_query)
