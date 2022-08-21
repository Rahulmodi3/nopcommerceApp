from selenium import webdriver
import pytest
import chromedriver_autoinstaller
from webdriver_manager.firefox import GeckoDriverManager
import os


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
            screenshot = driver.get_screenshot_as_base64() # the hero
            extra.append(pytest_html.extras.image(screenshot, ''))


        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture
def setup(broswer):

    global driver
    if broswer == 'chrome':
        chromedriver_autoinstaller.install() # auto dowanload new driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching Chrome browser ...........")

    if broswer == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching Firefox browser ...........")

    else:     # if not pass browser name than run by defualt chorme browser
        chromedriver_autoinstaller.install()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)

    return driver

def pytest_addoption(parser):    # This wrill get the value from CLI/hooks
    parser.addoption("--browsername") # --browsername  which will pass through cmd line

@pytest.fixture()
def broswer(request):            # This will return the browser value to setpup method
    return request.config.getoption("--browsername")
