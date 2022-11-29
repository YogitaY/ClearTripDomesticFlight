from selenium import webdriver
import time
import pytest
from library_.config import Config
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["Chrome"])
def _driver(request):
    if request.param == "Chrome":
        driver_1 = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
        time.sleep(3)

    # elif request.param == "Edge":
    #     driver_1 = webdriver.Edge(EdgeChromiumDriverManager().install())
    #     time.sleep(3)
    #
    # elif request.param == "Firefox":
    #
        # driver_1 = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path)


    driver_1.get(Config.Url)
    time.sleep(2)
    driver_1.maximize_window()
    time.sleep(2)
    yield driver_1
    print(driver_1.title)
    time.sleep(2)

    # driver_1.save_screenshot("text_loginpage.png")

    driver_1.close()


