from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .request_page import RequestPage

class MainPage(BasePage):
    def go_to_request_page(self):
        request = self.browser.find_element(*MainPageLocators.REQUEST_LINK)
        request.click()
        return RequestPage(browser=self.browser, url=self.browser.current_url)

    def should_be_request_link(self):
        assert self.browser.find_element(*MainPageLocators.REQUEST_LINK),'should be request link'

    def should_be_facebook_link(self):
        assert self.browser.find_element(*MainPageLocators.FACEBOOK_LINK),'should be facebook link'

    def should_be_instagram_link(self):
        assert self.browser.find_element(*MainPageLocators.INSTAGRAM_LINK),'should be instagram link'

    def should_be_linkedin_link(self):
        assert self.browser.find_element(*MainPageLocators.LINKEDIN_LINK),'should be linkedin link'

    def go_to_facebook_page(self):
        facebook = self.browser.find_element(*MainPageLocators.FACEBOOK_LINK)
        facebook.click()

    def go_to_instagram_page(self):
        instagram = self.browser.find_element(*MainPageLocators.INSTAGRAM_LINK)
        instagram.click()


    def go_to_linkedin_page(self):
        linkedin = self.browser.find_element(*MainPageLocators.LINKEDIN_LINK)
        linkedin.click()

    def should_be_languages_link(self):
        assert self.browser.find_element(*MainPageLocators.LANGUAGES_LINK),'should be languages link'


    def should_be_clients_link(self):
        assert self.browser.find_element(*MainPageLocators.CLIENTS_LINK),'should be clients link'

    def go_to_clients_link(self):
        clients = self.browser.find_element(*MainPageLocators.CLIENTS_LINK)
        clients.click()


    def should_be_about_us_link(self):
        assert self.browser.find_element(*MainPageLocators.ABOUTUS_LINK),'should be about us link'

    def go_to_about_us_link(self):
        clients = self.browser.find_element(*MainPageLocators.ABOUTUS_LINK)
        clients.click()

    def should_be_our_service_link(self):
        assert self.browser.find_element(*MainPageLocators.OURSERVICE_LINK),'should be our service link'

    def go_to_our_service_link(self):
        service = self.browser.find_element(*MainPageLocators.OURSERVICE_LINK)
        service.click()