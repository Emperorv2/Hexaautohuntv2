```python
from modules.scraper import Scraper
from modules.automation import Automation
import utils.logger as logger

def main():
    logger.info("Starting HexaAutohunt")
    scraper = Scraper()
    scraper.run()
    
    automation = Automation()
    automation.run()

if __name__ == "__main__":
    main()