import scrape_data


def test_extract_links_length():
    """
    Validate number of parsed documents against number visible on the scrape url website

    Right now it's 79, validated manually against the scrape URL.
    """
    scrape_url = "https://pa.gov/agencies/dli/programs-services/workers-compensation/wc-health-care-services-review/wc-fee-schedule/part-b-fee-schedules.html"
    assert len(scrape_data.extract_links(scrape_url)) == 79
