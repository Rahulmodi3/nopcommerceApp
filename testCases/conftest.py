from selenium import webdriver
import pytest
#import chromedriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

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

# This will open chrome browser in incognito mode
def openchrome():

    #chromedriver_autoinstaller.install() # auto dowanload new driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=chrome_options)

# This will open chrome in headless mode
def headlesschrome():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=chrome_options)

def headlessfirefix():

    options = Options()
    options.headless = True
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    #options.add_argument('window-size=1920x1080')
    return webdriver.Firefox(options=options,service=FirefoxService(GeckoDriverManager().install()))


@pytest.fixture
def setup(broswer):

    global driver
    if broswer == 'chrome':

        driver = openchrome() #calling openchrome function
        print("Launching Chrome browser ...........")

    elif broswer == 'firefox':

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser ...........")

    elif broswer == 'chromeheadless':

        driver = headlesschrome() #calling headlesschrome function

        print("Launching Chrome in headless mode ...........")

    elif broswer == 'firefoxheadless':
        driver = headlessfirefix()
        print("Launching Firefox in headless mode ...........")

    else:     # if not pass browser name than run by defualt chorme browser

        driver = openchrome() #calling openchrome function
        print("Launching Chrome browser ...........")

    return driver

def pytest_addoption(parser):    # This wrill get the value from CLI/hooks
    parser.addoption("--browsername") # --browsername  which will pass through cmd line


@pytest.fixture()
def broswer(request):            # This will return the browser value to setpup method
    return request.config.getoption("--browsername")
