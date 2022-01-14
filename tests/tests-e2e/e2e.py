from utils.driverfactory import make_driver
import time

processes = "//*[@id='process_tab']//tr"


def open_url(driver, url=None):
    driver.get(url)
    time.sleep(10)


def check_process_info(driver):
    return len(driver.find_elements_by_xpath(processes))


if __name__ == "__main__":
    driver = make_driver(remote=False)
    open_url(driver, url="http://localhost:5000/monitor")
    assert check_process_info(driver) > 10
