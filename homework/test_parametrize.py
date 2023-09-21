from selene import browser, be

from homework.conftest import desktop_only, mobile_only

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@desktop_only
def test_github_desktop(browser_opt):
    browser.open('')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)


@mobile_only
def test_github_mobile(browser_opt):
    browser.open('')

    browser.element('.flex-order-2 .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)
