from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.options import Options

SELENIUM_HUB = "localhost"


def make_driver(remote=True):
    """
    Returns a chromedriver for the given arguments
    """
    url = "http://{host}:{port}/wd/hub".format(host=SELENIUM_HUB, port="4444")

    # options = _get_firefox_options()
    options = _get_chrome_options()

    capabilities = options.to_capabilities()
    capabilities["enableVNC"] = True
    capabilities["enableVideo"] = True
    capabilities["sessionTimeout"] = "20m"

    if remote:
        driver = webdriver.Remote(url, desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(options=options)
    return driver


def _get_chrome_options():
    """
    Returns the chrome options for the following arguments
    """
    chrome_options = Options()

    # Standard options
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--auto-select-desktop-capture-source=Entire screen")
    chrome_options.add_argument('--headless')
    return chrome_options


def _get_firefox_options():
    """
    Returns the firefox options for the following arguments
    """
    firefox_options = webdriver.FirefoxOptions()

    # Standard options
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-notifications")
    return firefox_options
