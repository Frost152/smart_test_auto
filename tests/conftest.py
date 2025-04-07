import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver

