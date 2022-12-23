import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from params.parameters import TestParams

@pytest.fixture(autouse=True)
def init_driver(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(1)
    request.cls.driver = driver
    driver.get(TestParams.BASE_URL)
