import requests


def scrape_data(url):
    return False


if __name__ == "__main__":
    scrape_url = "https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html"
    print(scrape_data(scrape_url))
    print(requests.get(scrape_url).content)
