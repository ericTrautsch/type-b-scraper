import os
import requests

from bs4 import BeautifulSoup


def extract_links(url: str) -> list:
    """
    Extracts links for relative download urls for part b fee schedules.
    """
    hostname = "/".join(url.split("/")[0:3])
    # TODO: Determine headers (if needed)
    headers = {}

    # Get top-level page and create parser
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all cmp-buttons
    buttons = soup.find_all("a", class_="cmp-button")

    # Extract links
    links = [hostname + button["href"] for button in buttons if "href" in button.attrs]
    return links


def download_file(link: str, save_dir: str) -> bool:
    """
    Downloads file using chunked strategy
    """
    # TODO: Determine headers (if needed)
    headers = {}
    response = requests.get(link, headers)
    if response.status_code == 200:
        print("./data/" + link.split("/")[-1])
        with open(("./data/" + link.split("/")[-1]), "wb") as file:
            file.write(response.content)
        return True
    else:
        return False


if __name__ == "__main__":
    scrape_url = "https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html"
    links = extract_links(scrape_url)
    print(links)
    print(download_file(links[-1], "../data/"))
