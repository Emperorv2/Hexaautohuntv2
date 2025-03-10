from selenium import webdriver
from utils.logger import logger
from utils.config import CONFIG

class Automation:
    def __init__(self):
        options = webdriver.ChromeOptions()
        if CONFIG["HEADLESS"]:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def run(self):
        logger.info("Starting automation")
        self.driver.get(CONFIG["SCRAPER_URL"])
        logger.info("Automation completed")
        self.driver.quit()