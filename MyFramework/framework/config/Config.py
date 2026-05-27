import os

class Config:
    # Application URLs
    BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"

    # Browser settings
    BROWSER = "chromium"  # options: chromium, firefox, webkit
    # Default False (headed) locally, but CI sets HEADLESS=true
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Timeout settings
    DEFAULT_TIMEOUT = 30000  # in ms

    # Report paths
    REPORT_DIR = "reports/"
    SCREENSHOT_DIR = REPORT_DIR + "screenshots/"

    # Test data paths
    TEST_DATA_FILE = "data/test_data.json"
    LOCATORS_FILE = "data/locators.json"
