import pytest
from MyFramework.framework.config.Config import Config

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.failed and "page" in item.funcargs:
        page = item.funcargs["page"]
        page.screenshot(path=f"{Config.SCREENSHOT_DIR}/{item.name}_failed.png")
