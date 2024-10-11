from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_burgers import BurgersLocators

class TestBurgersRegistration:
    def test_registration_correct(self, driver, user_data):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*BurgersLocators.NAME_INPUT_FIELD).send_keys(user_data['name'])
        driver.find_element(*BurgersLocators.EMAIL_INPUT_FIELD).send_keys(user_data['email'])
        driver.find_element(*BurgersLocators.PASSWORD_INPUT_FIELD).send_keys(user_data['password'])
        driver.find_element(*BurgersLocators.REGISTRATION_BUTTON_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.LOGIN_HEADER)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_registration_incorrect(self, driver, user_data_incorrect):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*BurgersLocators.NAME_INPUT_FIELD).send_keys(user_data_incorrect['name'])
        driver.find_element(*BurgersLocators.EMAIL_INPUT_FIELD).send_keys(user_data_incorrect['email'])
        driver.find_element(*BurgersLocators.PASSWORD_INPUT_FIELD).send_keys(user_data_incorrect['password'])
        driver.find_element(*BurgersLocators.REGISTRATION_BUTTON_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.INCORRECT_PASSWORD_ERROR)))
        password_error = driver.find_element(*BurgersLocators.INCORRECT_PASSWORD_ERROR).text
        assert password_error == 'Некорректный пароль'

