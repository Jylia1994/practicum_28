import time
from modyl_26.pages.auth_page import AuthPage


def test_registration(web_browser):
    """Проверяем форму регистрации а так же,как система будет реагировать на некорретные данные от пользовтеля"""

    page = AuthPage(web_browser)

    page.btn_register.click()
    page.firstName.click()
    page.firstName.send_keys("Vasia")

    page.lastName.click()
    page.lastName.send_keys("Pypkin")

    page.address.click()
    page.address.send_keys('vasia@')

    page.new_password.click()
    page.new_password.send_keys('12345678')

    page.password_confirm.click()
    page.password_confirm.send_keys('12345678')

    page.submit.click()


def test_phone_number(web_browser):
    """Авторизация по номеру телефона(в целях своей безопасности от возможных спамеров свой номер телефона оставлять
    не стала,а лишнего номера нет)"""

    page = AuthPage(web_browser)
    page.btn_phone.click()

    page.phone_number.send_keys('''Номер зарегистрированный на сайте''')
    page.password.send_keys('12345678Da')

    page.btn_sing_in.click()


def test_email(web_browser):
    """Авторизация по почте и паролю"""

    page = AuthPage(web_browser)
    page.btn_mail.click()

    page.email.send_keys('volkdarina94@gmail.com')
    page.password.send_keys('12345678Da')

    page.btn_sing_in.click()


def test_login(web_browser):
    """Авторизауия по логин и паролю(логин взят из аккаунта теста вход по почте"""

    page = AuthPage(web_browser)
    page.btn_login.click()
    time.sleep(2)
    page.login.send_keys('rtkid_1690200198214')
    page.password.send_keys('12345678Da')

    page.btn_sing_in.click()


def test_ls(web_browser):
    """Авторизауия по лицевому счету и паролю(тест создан по аналогии с другими способами входа, по логике должен
    работать)"""

    page = AuthPage(web_browser)
    page.btn_ls.click()
    time.sleep(2)
    page.ls.send_keys('rtkid_1690200198214')
    page.password.send_keys('12345678Da')

    page.btn_sing_in.click()


def test_tab_email(web_browser):
    """Проверка автоматического таба (переход со строки телефон на строку почта)"""

    page = AuthPage(web_browser)

    page.btn_phone.click()
    time.sleep(3)
    page.email.send_keys('volkdarina94@gmail.com')
    page.password.click()


def test_tab_phone_number(web_browser):
    """Проверка автоперехода со строки почта на строку телефон"""
    page = AuthPage(web_browser)

    page.btn_mail.click()
    time.sleep(3)
    page.phone_number.send_keys('+79852564766')
    page.password.click()


def test_tab_login(web_browser):
    """Проверка автоперехода со строки телефон на строку логин"""
    page = AuthPage(web_browser)

    page.btn_phone.click()
    time.sleep(3)
    page.login.send_keys('rtkid_1690200198214')
    page.password.click()


def test_click(web_browser):
    """Проверка нижних иконок на переход на сторонние соцсети"""

    page = AuthPage(web_browser)

    page.vk.click()
    time.sleep(5)
    page.go_back()

    page.ok.click()
    time.sleep(5)
    page.go_back()

    page.mail.click()
    time.sleep(5)
    page.go_back()

    page.yandex.click()
    time.sleep(10)
    page.go_back()


def test_email_negative(web_browser):
    """Попытка входа с некорректными данными(почта на неправильная)"""

    page = AuthPage(web_browser)
    page.btn_mail.click()

    page.email.send_keys('volkdarina@gmail.com')
    page.password.send_keys('12345678Da')

    page.btn_sing_in.click()


def test_password_negative(web_browser):
    """Попытка входа с неправильным паролем"""

    page = AuthPage(web_browser)

    page.email.send_keys('volkdarina94@gmail.com')
    page.password.send_keys('87654321Da')

    page.btn_sing_in.click()
