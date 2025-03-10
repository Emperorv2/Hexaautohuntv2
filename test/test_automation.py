import unittest
from src.modules.automation import Automation

class TestAutomation(unittest.TestCase):
    def test_automation(self):
        automation = Automation()
        self.assertIsNotNone(automation.driver)

if __name__ == "__main__":
    unittest.main()