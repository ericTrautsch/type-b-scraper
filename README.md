# Part B Fee Schedule Scraper PoC

## Overview

Run locally extract Part B schedules from [Part B Schedules](https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html) and collect output in a single `.csv` file.

## Scope

For the initial proof of concept, this scraper is built to run locally produce output in a single `.csv` file.

## Getting Started

1. Run via `python` 

2. Run via Docker

## Details

### Data Scraping

Part B Fee Schedules are scraped and downloaded in [`src/scrape_data.py`](./src/scrape_data.py). Files are downloaded to a top-level `data/` directory to store these files.


