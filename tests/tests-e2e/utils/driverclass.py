import os
import platform
import logging
from selenium import webdriver
from conftest import get_project_root

PROJECT_ROOT = get_project_root()

plt = platform.system()

if plt == "Windows":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT, "tests", "tests-e2e", 'utils', "Chromedrivers", "Windows",
                                       "chromedriver.exe")
elif plt == "Linux":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT, "tests", "tests-e2e", 'utils', "Chromedrivers", "Linux",
                                       "chromedriver")
elif plt == "Darwin":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT, "tests", "tests-e2e", 'utils', "Chromedrivers", "Mac",
                                       "chromedriver")
else:
    logging.exception("Unsupported Platform")


class driverClass():
    @staticmethod
    def register_driver():
        return driverClass.get_web_driver()

    @staticmethod
    def get_web_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--headless')
        Chrome = webdriver.Chrome(ChromeDriverExePath, options=chrome_options)
        Chrome.implicitly_wait(2)
        return Chrome
