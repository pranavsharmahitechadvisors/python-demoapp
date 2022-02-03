from pagebase import PageBase
from selenium.common.exceptions import TimeoutException
from random import uniform
from time import sleep
import time
from datetime import datetime
from os import environ
import os


# from dotenv import load_dotenv
#
# load_dotenv("../../.envSS")  # only for local debug

# LOGIN_USER, LOGIN_PASSWORD = environ["LOGIN_USER"], environ["LOGIN_PASSWORD"]
# BASE_URL = "https://www.linkedin.com/login"


class HomePage(PageBase):
    def __init__(self, selenium_driver="NAN", url=None):
        PageBase.__init__(self, selenium_driver, url=url)

    info_btn = "xpath@@//a[@href='/info']"
    sys_info = "xpath@@//h1[contains(text(),'System Information')]"
    hostname = "xpath@@/html/body/div/div/table/tbody/tr[1]/td[2]"
    os_pltform = "xpath@@/html/body/div/div/table/tbody/tr[3]/td[2]"

    def show_info(self):
        """
        """
        self.click(self.info_btn)
        self.wait_till_element_is_present(self.sys_info)
        print("Hostname is {}".format(self.get_text(self.hostname)))
        print("OS Platform is {}".format(self.get_text(self.os_pltform)))
