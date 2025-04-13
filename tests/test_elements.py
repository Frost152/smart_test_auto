from pages.elements_page import PageTextBox, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage
import time


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

    class TestWebTables:
        def test_add_person_in_table(self, driver):
            table_page = WebTablePage(driver)
            table_page.open("https://demoqa.com/webtables")
            table_page.complete_reg_form()

        def test_many_add_person(self, driver):
            table_page = WebTablePage(driver)
            table_page.open("https://demoqa.com/webtables")
            fields = table_page.many_reg_form(2)
            print(table_page.get_line_for_index(3))
            table_page.click_edit_button_for_index(2)
            table_page.clear_all_fields()
            time.sleep(1)
            table_page.send_age_field()
            table_page.click_submit_button()
            table_page.send_search(list(fields)[0]["first_name"])
            table_page.choice_all_elements_pagination()

    class TestAllClick:
        def test_all_click(self, driver):
            page = ButtonsPage(driver)
            page.open("https://demoqa.com/buttons")
            page.all_ckick()


    class TestLinks:
        def test_links(self, driver):
            page = LinksPage(driver)
            page.open("https://demoqa.com/links")
            page.final_link()