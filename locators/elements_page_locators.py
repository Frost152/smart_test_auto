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
    all_checking_check_box = (
        By.XPATH, "//*[contains(@class, 'rct-icon-check')]//ancestor::span[contains(@class, 'rct-text')]")
    all_success_elements = (By.CSS_SELECTOR, ".text-success")


class RadButtonLocators:
    yes_radio = (By.CSS_SELECTOR, "label[for='yesRadio']")
    impressive_radio = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    no_radio = (By.CSS_SELECTOR, "label[for='noRadio'")
    text_success = (By.CSS_SELECTOR, ".text-success")


class WebTableLocators:
    class Table:
        add_button = (By.CSS_SELECTOR, "#addNewRecordButton")
        user_string = (By.XPATH, "(//div[contains(@class, 'rt-tr-group') and .//span[@title='Edit']])")
        edit_button = (By.XPATH, ".//span[@title='Edit']")
        delete_button = (By.XPATH, "//span[@title='Delete']")
        pagination = (By.XPATH, "//select")

    class AddForm:
        first_name = (By.CSS_SELECTOR, "#firstName")
        last_name = (By.CSS_SELECTOR, "#lastName")
        email = (By.CSS_SELECTOR, "#userEmail")
        age = (By.CSS_SELECTOR, "#age")
        salary = (By.CSS_SELECTOR, "#salary")
        department = (By.CSS_SELECTOR, "#department")
        submit_button = (By.CSS_SELECTOR, "#submit")


class ButtonsPageLocators:
    double = (By.CSS_SELECTOR, "#doubleClickBtn")
    right = (By.CSS_SELECTOR, "#rightClickBtn")
    click = (By.XPATH, "//button[text()='Click Me']")