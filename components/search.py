import selenium
from components.base import Base


class Search(Base):
    search_field_xpath = "//input[@data-testid='search-bar']"
    search_button_xpath = "//button[@type='submit']"

    def search_field_input(self, user_name):
        self.input_into_text_field(user_name, self.search_field_xpath)

    def click_search_button(self):
        self.click(self.search_button_xpath)
