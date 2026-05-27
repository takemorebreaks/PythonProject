import os

import playwright.sync_api
from playwright.sync_api import sync_playwright

from MyFramework.framework.config.Config import Config
from MyFramework.framework.logger.Logger import Logger


class BaseTest:
    log = Logger.get_logger()
    log.info("Starting Base test class")
    def setup_method(self):
        self.playwright = sync_playwright().start()
        # Pick browser dynamically from Config
        browser_type = getattr(self.playwright,Config.BROWSER)
        self.browser = browser_type.launch(headless=Config.HEADLESS)
        self.page=self.browser.new_page()
        self.page.set_default_timeout(Config.DEFAULT_TIMEOUT)
        self.page.goto(Config.BASE_URL)
        self.log.info(f"Browser launched: {Config.BROWSER}, Headless={Config.HEADLESS}")
        self.log.info(f"Navigated to {Config.BASE_URL}")

    def teardown_method(self, method):
        if hasattr(self, "page") and self.page:
            if hasattr(method, "__name__") and self._outcome.errors:
                os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
                self.page.screenshot(
                    path=f"{Config.SCREENSHOT_DIR}/{method.__name__}_failed.png"
                )
        self.browser.close()
        self.playwright.stop()
