from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def make_driver(SELENIUM_HUB="localhost", headless=False, vnc=True, remote=True):
    """
    Returns a chromedriver for the given arguments
    """
    url = "http://{host}:{port}/wd/hub".format(host=SELENIUM_HUB, port="4444")

    options = _get_chrome_options()
    if headless:
        options.add_argument("--headless")

    capabilities = options.to_capabilities()
    capabilities["pageLoadStrategy"] = "none"
    if vnc:
        capabilities["enableVNC"] = True
        capabilities["sessionTimeout"] = "5m"

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
    # chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--auto-select-desktop-capture-source=Entire screen")
    return chrome_options
