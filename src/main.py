import scrape_data
import process
import sys


def execute_scraper():
    scrape_data.scrape_data()

    if len(sys.argv) > 1:
        process.process(pdf_folder="./data", output_path=sys.argv[1])
    else:
        process.process()


if __name__ == "__main__":
    execute_scraper()
