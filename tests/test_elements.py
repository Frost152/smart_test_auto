from pages.elements_page import PageTextBox


class TestElements:
    class TestTextBox:
        def test(self, driver):
            page = PageTextBox(driver)
            page.open("https://demoqa.com/text-box")
            page.fill_text_box()
