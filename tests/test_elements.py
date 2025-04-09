from pages.elements_page import PageTextBox, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            page = PageTextBox(driver)
            page.open("https://demoqa.com/text-box")
            page.fill_text_box()

    class TestCheckBox:
        def test_check_box(self, driver):
            page = CheckBoxPage(driver)
            page.open("https://demoqa.com/checkbox")
            page.random_click_checkboxes()

    class TestRadioButton:
        def test_radio_button(self, driver):
            page = RadioButtonPage(driver)
            page.open('https://demoqa.com/radio-button')
            page.choice_radio('Impressive')
            page.choice_radio('Yes')