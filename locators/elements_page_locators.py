from selenium.webdriver.common.by import By


class TestBoxLocators:
    full_name = (By.XPATH, "//input[@id='userName']")
    email = (By.XPATH, "//input[@id='userEmail']")
    current_address = (By.XPATH, "//textarea[@id='currentAddress']")
    permanent_address = (By.XPATH, "//textarea[@id='permanentAddress']")
    submit_button = (By.CSS_SELECTOR, "#submit")

    name_output = (By.CSS_SELECTOR, "#name")
    email_output = (By.CSS_SELECTOR, "#email")
    current_address_output = (By.CSS_SELECTOR, "p#currentAddress")
    permanent_address_output = (By.CSS_SELECTOR, "p#permanentAddress")