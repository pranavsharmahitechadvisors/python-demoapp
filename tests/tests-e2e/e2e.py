from utils.driverclass import driverClass
from selenium.webdriver.common.by import By
import time

processes = "//*[@id='process_tab']//tr"


def open_url(driver, url=None):
    print("opening url {}".format(url))
    driver.get(url)
    print("Waiting for 30 seconds {}".format(url))
    time.sleep(30)


def check_process_info(driver):
    num_process_running = len(driver.find_elements(By.XPATH, value=processes))
    print("{} Number of processes are currently running on the system".format(num_process_running))
    return num_process_running


if __name__ == "__main__":
    print("Initializing chromedriver")
    driver = driverClass.register_driver()
    print("Running E2E test to check the processes information")
    open_url(driver, url="http://localhost:5000/monitor")
    assert check_process_info(driver) > 10
    print("Test Verified Succesfully")
    driver.quit()
