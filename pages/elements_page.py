from base.base_class import Base
from locators.elements_page_locators import TestBoxLocators
from locators.elements_page_locators import CheckBoxLocators
from locators.elements_page_locators import RadButtonLocators
from generator import generator
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
