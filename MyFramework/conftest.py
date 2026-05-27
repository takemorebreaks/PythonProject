import shutil
import pytest
import os
from MyFramework.framework.config.Config import Config
from MyFramework.framework.logger.Logger import Logger

log = Logger.get_logger("pytest_hooks")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        test_instance = getattr(item, "instance", None)
        if test_instance and hasattr(test_instance, "page"):
            os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
            screenshot_path = f"{Config.SCREENSHOT_DIR}/{item.name}_failed.png"
            test_instance.page.screenshot(path=screenshot_path)
            log.info(f"Screenshot captured for failed test: {item.name} → {screenshot_path}")
        else:
            log.warning(f"Failed test {item.name} has no page object, screenshot skipped.")

@pytest.fixture(scope="session", autouse=True)
def clean_and_create_report_dirs():
    log.info("Preparing report directories at session start...")

    # Remove old screenshots folder if it exists
    if os.path.exists(Config.SCREENSHOT_DIR):
        shutil.rmtree(Config.SCREENSHOT_DIR)
        log.info(f"Deleted old screenshot directory: {Config.SCREENSHOT_DIR}")

    # Recreate fresh directories
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(Config.REPORT_DIR, exist_ok=True)

    log.info(f"Created fresh screenshot directory: {Config.SCREENSHOT_DIR}")
    log.info(f"Ensured report directory exists: {Config.REPORT_DIR}")
