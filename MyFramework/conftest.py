import shutil

import pytest
import os
from MyFramework.framework.config.Config import Config

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    test_instance = getattr(item, "instance", None)
    if test_instance and hasattr(test_instance, "page"):
        page = test_instance.page
        if page:
            os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
            page.screenshot(path=f"{Config.SCREENSHOT_DIR}/{item.name}_failed.png")
    else:
        page = None

@pytest.fixture(scope="session", autouse=True)
def clean_and_create_report_dirs():
    # Remove old screenshots folder if it exists
    if os.path.exists(Config.SCREENSHOT_DIR):
        shutil.rmtree(Config.SCREENSHOT_DIR)
    # Recreate fresh directories
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(Config.REPORT_DIR, exist_ok=True)
