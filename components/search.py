import selenium
from components.base import Base
from components.xpath_locators import Locators


class Search(Base):
    search_field_xpath = Locators.search_input
    search_button_xpath = Locators.search_button

    def search_field_input(self, user_name):
        self.input_into_text_field(user_name, self.search_field_xpath)

    def click_search_button(self):
        self.click(self.search_button_xpath)
