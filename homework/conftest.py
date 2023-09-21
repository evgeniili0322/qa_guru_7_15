import pytest

from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', params=[
    pytest.param('1920,1080', id='FullHD'),
    pytest.param('2560,1440', id='2k'),
    pytest.param('4096,2160', id='4k'),
])
def browser_opt_desktop(request):
    options = webdriver.ChromeOptions()

    options.add_argument(f'window-size={request.param}')

    browser.config.base_url = 'https://github.com/'
    browser.config.driver_options = options

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[
    pytest.param('390,844', id='iPhone 14'),
    pytest.param('430,932', id='iPhone 14 Pro Max'),
    pytest.param('360,780', id='Samsung s23')
])
def browser_opt_mobile(request):
    options = webdriver.ChromeOptions()

    options.add_argument(f'window-size={request.param}')

    browser.config.base_url = 'https://github.com/'
    browser.config.driver_options = options

    yield

    browser.quit()


def pytest_configure():
    pytest.resolution = ''


@pytest.fixture(scope='function', params=[
    pytest.param('1920,1080', id='FullHD'),
    pytest.param('2560,1440', id='2k'),
    pytest.param('4096,2160', id='4k'),
    pytest.param('390,844', id='iPhone 14'),
    pytest.param('430,932', id='iPhone 14 Pro Max'),
    pytest.param('360,780', id='Samsung s23')
])
def browser_opt(request):
    pytest.resolution = request.param

    options = webdriver.ChromeOptions()
    options.add_argument(f'window-size={pytest.resolution}')

    browser.config.base_url = 'https://github.com/'
    browser.config.driver_options = options

    yield

    browser.quit()


# Screen resolution parameters
desktop_only = pytest.mark.parametrize('browser_opt', ['1920,1080', '2560,1440', '4096,2160'],
                                       ids=['FullHD', '2k', '4k'], indirect=True)

mobile_only = pytest.mark.parametrize('browser_opt', ['390,844', '430,932', '360,780'],
                                      ids=['iPhone 14', 'iPhone 14 Pro Max', 'Samsung s23'], indirect=True)
