from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_burgers import BurgersLocators

class TestBurgersPersonalAccount:
    #переход по клику на «Личный кабинет»:
    def test_click_on_personal_account_button(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGIN_HEADER)))
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_INPUT_FIELD).send_keys(exist_user_data['email'])
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_INPUT_FIELD).send_keys(exist_user_data['password'])
        driver.find_element(*BurgersLocators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGOUT_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    #Переход из личного кабинета по клику на «Конструктор»:
    def test_click_on_constructor(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_INPUT_FIELD).send_keys(exist_user_data['email'])
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_INPUT_FIELD).send_keys(exist_user_data['password'])
        driver.find_element(*BurgersLocators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGOUT_BUTTON)))
        driver.find_element(*BurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    #Переход по клику на логотип Stellar Burgers
    def test_click_on_logo(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_INPUT_FIELD).send_keys(exist_user_data['email'])
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_INPUT_FIELD).send_keys(exist_user_data['password'])
        driver.find_element(*BurgersLocators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGOUT_BUTTON)))
        driver.find_element(*BurgersLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    #Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_click_on_logout_button(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*BurgersLocators.LOGIN_EMAIL_INPUT_FIELD).send_keys(exist_user_data['email'])
        driver.find_element(*BurgersLocators.LOGIN_PASSWORD_INPUT_FIELD).send_keys(exist_user_data['password'])
        driver.find_element(*BurgersLocators.LOGIN_APPLY_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.MAKE_ORDER_BUTTON)))
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGOUT_BUTTON)))
        driver.find_element(*BurgersLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGIN_HEADER)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'



