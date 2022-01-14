import os
import platform
import logging
from selenium import webdriver

PROJECT_ROOT = os.path.join(os.path.dirname(__file__))

plt = platform.system()

if plt == "Windows":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT,  "Chromedrivers", "Windows",
                                       "chromedriver.exe")
elif plt == "Linux":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT, "Chromedrivers", "Linux",
                                       "chromedriver")
elif plt == "Darwin":
    ChromeDriverExePath = os.path.join(PROJECT_ROOT, "Chromedrivers", "Mac",
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
