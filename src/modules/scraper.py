import requests
from bs4 import BeautifulSoup
from utils.logger import logger
from utils.config import CONFIG

class Scraper:
    def __init__(self):
        self.url = CONFIG["SCRAPER_URL"]

    def run(self):
        logger.info(f"Scraping {self.url}")
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            logger.info("Scraping successful")
        else:
            logger.error("Failed to scrape the website")