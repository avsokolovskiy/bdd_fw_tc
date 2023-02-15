from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


DRIVER_SERVICE = Service(executable_path=ChromeDriverManager().install())


def get_driver(browser: str, resolution_h: int, resolution_w: int) -> webdriver:

    if browser.upper() == "CH":
        print("Web Driver creation started.")
        driver = webdriver.Chrome(service=DRIVER_SERVICE)
    elif browser.upper() == "CH_HL":
        print("HL Web Driver creation started.")
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    else:
        raise KeyError(f"Unexpected browser {browser.upper()}")
    driver.set_window_size(width=resolution_w, height=resolution_h)
    print("Web Driver created.")

    return driver
