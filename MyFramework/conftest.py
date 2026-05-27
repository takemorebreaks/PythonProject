import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"reports/{item.name}.png")
