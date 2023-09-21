from selene import browser, be

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(browser_opt_desktop):
    browser.open('')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(browser_opt_mobile):
    browser.open('')

    browser.element('.flex-order-2 .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)
