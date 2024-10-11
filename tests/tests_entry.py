from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_burgers import BurgersLocators

class TestBurgersEntry:
    # вход по кнопке «Войти в аккаунт» на главной:
    def test_entry_main_page(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*BurgersLocators.LOGIN_BUTTON).click()
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

#вход через кнопку «Личный кабинет»:
    def test_personal_account_button(self, driver, exist_user_data):
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

#вход через кнопку в форме регистрации:
    def test_login_from_registration_form(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*BurgersLocators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
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

#вход через кнопку в форме восстановления пароля:
    def test_login_from_forgot_password_form(self, driver, exist_user_data):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*BurgersLocators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
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

