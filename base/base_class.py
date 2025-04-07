from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def elem_is_visibility(self, elem, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(elem))
        finally:
            pass

    def all_elem_is_visibility(self, elem, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(elem))

    def elem_is_presence(self, elem, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(elem))

    def all_elem_is_presence(self, elem, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(elem))

    def elem_clickable(self, elem, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(elem))

    def elem_not_visible(self, elem, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(elem))

    @staticmethod
    def assertion_text(exp, act):
        assert exp == act
