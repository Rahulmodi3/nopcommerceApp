from selenium  import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
driver = None

@pytest.fixture()
def setup(broswer):
    if broswer == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching Chrome browser ...........")

    if broswer == 'firefox':

        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=r'C:/Users/modir/PycharmProjects/Automation Framework/geckodriver.exe', options=options)
        print("Launching Firefox browser ...........")

    else:     # if not pass browser name than run by defualt chorme browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)

    return driver

def pytest_addoption(parser):    # This wrill get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def broswer(request):            # This will return the browser value to setpup method
    return request.config.getoption("--browser")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:/C:/SeleniumProject/Pytest_HTML_ScreenShot/ScreenShots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
    return driver


