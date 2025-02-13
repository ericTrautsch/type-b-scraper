from bs4 import BeautifulSoup
import requests


def extract_links(url):
    """
    Extracts links for relative download urls for part b fee schedules.
    """
    hostname = "/".join(url.split("/")[0:3])
    # TODO: Determine headers (if needed)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Get top-level page and create parser
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all cmp-buttons
    buttons = soup.find_all("a", class_="cmp-button")

    # Extract links
    links = [hostname + button["href"] for button in buttons if "href" in button.attrs]
    return links


if __name__ == "__main__":
    scrape_url = "https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html"
    links = extract_links(scrape_url)
    print(links)
