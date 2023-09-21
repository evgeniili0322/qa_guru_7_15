"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


def test_github_desktop(browser_opt):
    if pytest.resolution in ['390,844', '430,932', '360,780']:
        pytest.skip()

    browser.open('')

    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(browser_opt):
    if pytest.resolution in ['1920,1080', '2560,1440', '4096,2160']:
        pytest.skip()

    browser.open('')

    browser.element('.flex-order-2 .Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

    browser.element('.auth-form-body').should(be.visible)