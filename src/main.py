import scrape_data
import process


def execute_scraper():
    scrape_data.scrape_data()
    process.process()


if __name__ == "__main__":
    execute_scraper()
