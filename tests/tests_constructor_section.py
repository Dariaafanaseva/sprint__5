from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_burgers import BurgersLocators

class TestBurgersConstructionSection:
    #Проверка переходов к разделу «Соусы»
    def test_go_to_section_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*BurgersLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.SPACE_SAUCE_NAME)))
        space_sauce_name = driver.find_element(*BurgersLocators.SPACE_SAUCE_NAME).text
        assert space_sauce_name == 'Соус фирменный Space Sauce'

    #Проверка переходов к разделу «Начинки»
    def test_go_to_section_fillings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*BurgersLocators.FILLINGS_SECTION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.BEEF_FILLING_NAME)))
        beef_filling_name = driver.find_element(*BurgersLocators.BEEF_FILLING_NAME).text
        assert beef_filling_name == 'Говяжий метеорит (отбивная)'

    #Проверка переходов к разделу «Булки»
    def test_go_to_bun_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*BurgersLocators.FILLINGS_SECTION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.BEEF_FILLING_NAME)))
        driver.find_element(*BurgersLocators.BUN_SECTION).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((BurgersLocators.FLUORESCENT_BUN_NAME)))
        fluorescent_bun_name = driver.find_element(*BurgersLocators.FLUORESCENT_BUN_NAME).text
        assert fluorescent_bun_name == 'Флюоресцентная булка R2-D3'

