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
    # TODO: Fix edge cases better..
    links = [link for link in links if "pdf" in link]

    return links


def download_file(link: str, save_dir: str = "./data/") -> bool:
    """
    Downloads file using chunked strategy
    """
    # TODO: Determine headers (if needed)
    headers = {}
    response = requests.get(link, headers)
    # TODO: Should consider error handling beyond PoC
    if response.status_code == 200:
        print(save_dir + link.split("/")[-1])
        # TODO: Could consider a chunked download strategy in the future
        with open((save_dir + link.split("/")[-1]), "wb") as file:
            file.write(response.content)
        return True
    else:
        return False


def scrape_data():
    """
    Wrapper to handle data scraping as a whole (data scraping entrypoint)
    """
    scrape_url = "https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html"
    links = extract_links(scrape_url)
    if all([download_file(link) for link in links]):
        print("Successfully downloaded all files!")
    else:
        print("Failed to download all files successfully :(")


if __name__ == "__main__":
    scrape_data()
