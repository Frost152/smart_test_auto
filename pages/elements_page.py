from base.base_class import Base
from locators.elements_page_locators import TestBoxLocators
from generator import generator


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
