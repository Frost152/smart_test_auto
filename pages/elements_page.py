from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_class import Base
from locators.elements_page_locators import TestBoxLocators
from locators.elements_page_locators import CheckBoxLocators
from locators.elements_page_locators import RadButtonLocators
from locators.elements_page_locators import WebTableLocators as TBL
from locators.elements_page_locators import ButtonsPageLocators
from generator import generator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import random


class PageTextBox(Base):
    userProfile = next(generator.user_generate())

    def __init__(self, driver):
        super().__init__(driver)

    # Getters
    def get_full_name(self):
        return self.elem_clickable(TestBoxLocators.full_name)

    def get_email(self):
        return self.elem_clickable(TestBoxLocators.email)

    def get_current_address(self):
        return self.elem_clickable(TestBoxLocators.current_address)

    def get_permanent_address(self):
        return self.elem_clickable(TestBoxLocators.permanent_address)

    def get_submit_button(self):
        return self.elem_clickable(TestBoxLocators.submit_button)

    def get_name_output(self):
        return self.elem_is_presence(TestBoxLocators.name_output)

    def get_email_output(self):
        return self.elem_is_presence(TestBoxLocators.email_output)

    def get_current_address_output(self):
        return self.elem_is_presence(TestBoxLocators.current_address_output)

    def get_permanent_address_output(self):
        return self.elem_is_presence(TestBoxLocators.permanent_address_output)

    # Actions
    def send_full_name(self):
        self.get_full_name().send_keys(self.userProfile.name)

    def send_email(self):
        self.get_email().send_keys(self.userProfile.email)

    def send_current_address(self):
        self.get_current_address().send_keys(self.userProfile.current_address)

    def send_permanent_address(self):
        self.get_permanent_address().send_keys(self.userProfile.permanent_address)

    def click_submit_button(self):
        self.get_submit_button().click()

    def name_output_text(self):
        return self.get_name_output().text.split(':')[1]

    def email_output_text(self):
        return self.get_email_output().text.split(':')[1]

    def current_address_output_text(self):
        return self.get_current_address_output().text.split(':')[1]

    def permanent_address_output_text(self):
        return self.get_permanent_address_output().text.split(':')[1]

    # Metods
    def fill_text_box(self):
        self.send_full_name()
        self.send_email()
        self.send_current_address()
        self.send_permanent_address()
        self.click_submit_button()

        self.assertion_text(self.name_output_text(), self.userProfile.name)
        self.assertion_text(self.email_output_text(), self.userProfile.email)
        self.assertion_text(self.current_address_output_text(), self.userProfile.current_address)
        self.assertion_text(self.permanent_address_output_text(), self.userProfile.permanent_address)


class CheckBoxPage(Base):

    # Getters
    def get_all_button(self):
        return self.elem_clickable(CheckBoxLocators.all_button)

    def get_all_checkbox_elements(self):
        return self.all_elem_is_visibility(CheckBoxLocators.all_check_box_elements)

    def get_checking_checkbox_elements(self):
        return self.all_elem_is_visibility(CheckBoxLocators.all_checking_check_box)

    def get_selected_params(self):
        return self.all_elem_is_visibility(CheckBoxLocators.all_success_elements)

    # Actions
    def click_all_button(self):
        self.get_all_button().click()

    def click_random_checkbox_elements(self):
        elements = self.get_all_checkbox_elements()
        rand_check = random.randint(1, len(elements))
        for i in random.sample(elements, rand_check):
            i.click()

    def checking_checkbox_elements_text(self):
        for i in self.get_checking_checkbox_elements():
            yield i.text.lower().strip(".doc").replace(" ", "")

    def selected_params_text(self):
        for i in self.get_selected_params():
            yield i.text.lower().strip(".doc").replace(" ", "")

    # Methods

    def random_click_checkboxes(self):
        self.click_all_button()
        self.click_random_checkbox_elements()
        self.assertion_text(tuple(self.checking_checkbox_elements_text()), tuple(self.selected_params_text()))


class RadioButtonPage(Base):
    # Getters
    def get_radio_elem(self, name_elem):
        radio_elements = {'Yes': RadButtonLocators.yes_radio,
                          'No': RadButtonLocators.no_radio,
                          'Impressive': RadButtonLocators.impressive_radio
                          }
        return self.elem_is_presence(radio_elements[name_elem])

    def get_succes(self):
        return self.elem_clickable(RadButtonLocators.text_success)

    # Actions

    def click_radio_for_name(self, name_elem):
        self.get_radio_elem(name_elem).click()

    def text_field_succes(self):
        return self.get_succes().text

    # Methods
    def choice_radio(self, name_radio):
        self.click_radio_for_name(name_radio)
        self.assertion_text(name_radio, self.text_field_succes())


class WebTablePage(Base):
    userProfile = next(generator.user_generate())

    # Getters table
    def get_add_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(TBL.Table.add_button))

    def get_not_empty_lines(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(TBL.Table.user_string))

    def get_text_list_not_empty_lines(self):
        for i in self.get_not_empty_lines():
            yield i.text.splitlines()

    def get_last_not_empty_line(self):
        last_item = None
        for i in self.get_text_list_not_empty_lines():
            last_item = i
        return last_item

    def get_line_for_index(self, index):
        count = 1
        for i in self.get_text_list_not_empty_lines():
            if count == index:
                return i
            count += 1

    def get_elem_for_index(self, index):
        count = 1
        for i in self.get_not_empty_lines():
            if count == index:
                return i
            count += 1

    def get_edit_button_for_index(self, index):
        elem = self.get_elem_for_index(index)
        return elem.find_element(By.XPATH, ".//span[@title='Edit']")

    def get_search(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchBox")))

    def get_pagination(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.Table.pagination))

    # Actions table
    def click_add_button(self):
        self.get_add_button().click()

    def click_edit_button_for_index(self, index):
        self.get_edit_button_for_index(index).click()

    def send_search(self, param):
        self.get_search().send_keys(param)

    def choice_pagination_for_value(self, value):
        select = Select(self.get_pagination())
        select.select_by_value(value)

    # Getters form
    def get_first_name_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.first_name))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.last_name))

    def get_email_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.email))

    def get_age_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.age))

    def get_salary_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.salary))

    def get_department_field(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.department))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(TBL.AddForm.submit_button))

    # Actions form
    def send_first_name_field(self):
        first_name = self.userProfile.first_name
        self.get_first_name_field().send_keys(first_name)
        return first_name

    def clear_first_name_field(self):
        self.get_first_name_field().clear()

    def send_last_name_field(self):
        last_name = self.userProfile.last_name
        self.get_last_name_field().send_keys(last_name)
        return last_name

    def clear_last_name_field(self):
        self.get_last_name_field().clear()

    def send_email_field(self):
        email = self.userProfile.email
        self.get_email_field().send_keys(email)
        return email

    def clear_email_field(self):
        self.get_email_field().clear()

    def send_age_field(self):
        age = self.userProfile.age
        self.get_age_field().send_keys(age)
        return age

    def clear_age_field(self):
        self.get_age_field().clear()

    def send_salary_field(self):
        salary = self.userProfile.salary
        self.get_salary_field().send_keys(salary)
        return salary

    def clear_salary_field(self):
        self.get_salary_field().clear()

    def send_department_field(self):
        department = self.userProfile.department
        self.get_department_field().send_keys(department)
        return department

    def clear_department_field(self):
        self.get_department_field().clear()

    def click_submit_button(self):
        self.get_submit_button().click()

    # Methods form

    def clear_all_fields(self):
        self.clear_first_name_field()
        self.clear_last_name_field()
        self.clear_email_field()
        self.clear_age_field()
        self.clear_salary_field()
        self.clear_department_field()

    def filling_form(self):
        self.userProfile = next(generator.user_generate())

        first_name = self.send_first_name_field()
        last_name = self.send_last_name_field()
        email = self.send_email_field()
        age = self.send_age_field()
        salary = self.send_salary_field()
        department = self.send_department_field()
        self.userProfile = next(generator.user_generate())
        return {"first_name": first_name, "last_name": last_name, "email": email, "age": age, "salary": salary,
                "department": department}

    def complete_reg_form(self):
        self.click_add_button()
        fields = self.filling_form()
        self.click_submit_button()
        self.assertion_text(sorted(fields.values()), sorted(self.get_last_not_empty_line()))
        return fields

    def many_reg_form(self, count):
        for i in range(count):
            yield self.complete_reg_form()

    def choice_all_elements_pagination(self):
        elems = ["5", "20", "25", "50", "100"]
        for i in elems:
            self.choice_pagination_for_value(i)


class ButtonsPage(Base):

    # Getters
    def get_double(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ButtonsPageLocators.double))

    def get_right(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ButtonsPageLocators.right))

    def get_one(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(ButtonsPageLocators.click))

    # Actions

    def click_double(self):
        action = ActionChains(self.driver)
        action.double_click(self.get_double())
        action.perform()
        self.assertion_text(self.driver.find_element(By.CSS_SELECTOR, "#doubleClickMessage").text,
                            "You have done a double click")

    def click_right(self):
        action = ActionChains(self.driver)
        action.context_click(self.get_right()).perform()
        self.assertion_text(self.driver.find_element(By.CSS_SELECTOR, "#rightClickMessage").text,
                            "You have done a right click")

    def click_one(self):
        self.get_one().click()
        self.assertion_text(self.driver.find_element(By.CSS_SELECTOR, "#dynamicClickMessage").text,
                            "You have done a dynamic click")

    # Methods

    def all_ckick(self):
        self.click_double()
        self.click_right()
        self.click_one()
