import requests
from bs4 import BeautifulSoup

def scrape_page(url):

    try:
        response = requests.get(url, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return text[:3000]

    except:
        return ""