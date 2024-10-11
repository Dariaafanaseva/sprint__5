from selenium.webdriver.common.by import By

class BurgersLocators:
    #главная страница
    #кнопка "войти в аккаунт":
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    LOGIN_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    #кнопка "личный кабинет":
    ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/a/p']
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
    LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
    #страница регистрации, поля ввода:
    NAME_INPUT_FIELD = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')
    EMAIL_INPUT_FIELD = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')
    REGISTRATION_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    INCORRECT_PASSWORD_ERROR = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')
    #кнопка "Зарегистрироваться" на странице входа
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

    #страница входа, поля ввода и кнопка:
    LOGIN_EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="name"]')
    LOGIN_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    LOGIN_APPLY_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    #Кнопка оформить заказ на главной странице:
    MAKE_ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')

    #личный кабинет:
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')
    LOGO_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/div')

    #Выбор бургера:
    SAUCES_SECTION = (By.XPATH, '//span[text()="Соусы"]')
    SPACE_SAUCE_NAME = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[2]/p')
    FILLINGS_SECTION = (By.XPATH, '//span[text()="Начинки"]')
    BEEF_FILLING_NAME = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p')
    BUN_SECTION = (By.XPATH, '//span[text()="Булки"]')
    FLUORESCENT_BUN_NAME = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p')
