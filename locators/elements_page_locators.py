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


class CheckBoxLocators:
    all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
    all_check_box_elements = (By.CSS_SELECTOR, ".rct-checkbox")
    all_checking_check_box = (By.XPATH, "//*[contains(@class, 'rct-icon-check')]//ancestor::span[contains(@class, 'rct-text')]")
    all_success_elements = (By.CSS_SELECTOR, ".text-success")
