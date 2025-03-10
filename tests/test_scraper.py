import unittest
from src.modules.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_scraper(self):
        scraper = Scraper()
        self.assertIsNotNone(scraper.url)

if __name__ == "__main__":
    unittest.main()