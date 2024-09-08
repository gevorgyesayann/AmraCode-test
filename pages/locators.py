from selenium.webdriver.common.by import By


class MainPageLocators():
    REQUEST_LINK = (By.XPATH,'//*[@id="root"]/div/div[1]/button/a')
    FACEBOOK_LINK = (By.CSS_SELECTOR,'#root > div > div.footer_footer__KR8zb > div.footer_footerIcon__UNlop > ul > li:nth-child(2)')
    INSTAGRAM_LINK = (By.CSS_SELECTOR,'#root > div > div.footer_footer__KR8zb > div.footer_footerIcon__UNlop > ul > li:nth-child(1)')
    LINKEDIN_LINK = (By.CSS_SELECTOR,'#root > div > div.footer_footer__KR8zb > div.footer_footerIcon__UNlop > ul')
    LANGUAGES_LINK = (By.CSS_SELECTOR,'#root > div > div:nth-child(2) > nav > div > div:nth-child(3) > div > div:nth-child(2) > div > ul > li > div > div.dropdown_dropDownHeader__86a3j > img')
    CLIENTS_LINK = (By.CSS_SELECTOR,'html body div#root div.layout div nav.navbar_navbar__lsD-c div.navbar_nav__quB6-.navbar_nav_container__-cjKn div div.navbar_nav_menu__0TCQ2 div.navbar_en__6srmt div.navbar_nav_item__DGqne a.navbar_nav_links__QVmdN.false')
    ABOUTUS_LINK = (By.XPATH,'/html/body/div[2]/div/div[2]/nav/div/div[3]/div/div[1]/div[2]/a')
    OURSERVICE_LINK = (By.XPATH,'/html/body/div[2]/div/div[2]/nav/div/div[3]/div/div[1]/div[1]/a')
class RequestPagelocators():
    # FIRSTNAME = (By.CSS_SELECTOR,'[name="firstname"]')
    FIRSTNAME = (By.XPATH,'//*[@id="hsForm_f902d752-a8cd-4b5b-9c94-97d1b53e0dda"]/fieldset[3]/div[1]')
    LASTNAME = (By.XPATH,'//*[@id="hsForm_f902d752-a8cd-4b5b-9c94-97d1b53e0dda"]/fieldset[3]/div[2]')
