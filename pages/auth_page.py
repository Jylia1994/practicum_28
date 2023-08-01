from modyl_26.pages.base import WebPage
from modyl_26.pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else ('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id'
                               '=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type'
                               '=code&scope=openid&state=a4e528da-795d-4a5e-b2df-15ce5caf1d7b&theme&auth_type')
        super().__init__(web_driver, url)

    email = WebElement(id='username')
    phone_number = WebElement(id='username')
    login = WebElement(id='username')
    ls = WebElement(id='username')
    password = WebElement(id='password')
    '''Кнопка войти'''
    btn_sing_in = WebElement(id='kc-login')
    """Кнопка почта"""
    btn_mail = WebElement(id='t-btn-tab-mail')
    """Кнопка телефон"""
    btn_phone = WebElement(id='t-btn-tab-phone')
    """Кнопка логин"""
    btn_login = WebElement(id='t-btn-tab-login')
    '''Кнопка лицевой счет'''
    btn_ls = WebElement(id='t-btn-tab-ls')
    '''Кнопка регистрации'''
    btn_register = WebElement(id='kc-register')
    """Забыл пароль"""
    btn_forgot_pass = WebElement(id='forgot_password')
    """Форма регистрации"""
    firstName = WebElement(name='firstName')
    lastName = WebElement(name='lastName')
    address = WebElement(id='address')
    new_password = WebElement(name='password')
    password_confirm = WebElement(name='password-confirm')
    submit = WebElement(name='register')
    """Нижние иконки с переходом на соцсети"""
    vk = WebElement(id='oidc_vk')
    ok = WebElement(id='oidc_ok')
    mail = WebElement(id='oidc_mail')
    yandex = WebElement(id='oidc_ya')














