from .base_page import BasePage
from .locators import RequestPagelocators

class RequestPage(BasePage):
    def should_be_request_page(self):
        self.should_be_firstname_field()


    def should_be_firstname_field(self):
        assert self.is_element_present(*RequestPagelocators.FIRSTNAME),'should be firstname field'
        assert True


    def should_be_lastname_field(self):
        assert self.is_element_present(*RequestPagelocators.LASTNAME),'should be lastname field'
        assert True

