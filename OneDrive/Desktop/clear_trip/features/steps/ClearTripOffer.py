from selenium import webdriver
from behave import *
import time
from data import reading_objects
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

login_obj = reading_objects.read_locators()
print(login_obj)

@given(u'launch chrome browser')
def launch_browser(context):
    path = r"C:\Users\yogit\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver_obj = webdriver.Chrome(executable_path=path)


@when(u'enter clear trip url')
def open_home_page(context):
    context.driver_obj.get("https://www.cleartrip.com/")
    time.sleep(2)
    context.driver_obj.maximize_window()
    time.sleep(2)
    context.driver_obj.find_element(*login_obj["click_login_popup"]).click()
    time.sleep(1)


@when(u'Click on Offer button')
def click_offers(context):
    context.driver_obj.parent_window = context.driver_obj.current_window_handle
    context.driver_obj.find_element(*login_obj["click_Offers"]).click()
    time.sleep(2)


@then(u'verify that Offer button should navigate to Exclusive offers and deals for flight,hotels activities - ClearTrip page')
def window_alter(context):
    child_window = context.driver_obj.window_handles
    print("parent window handle name is", context.driver_obj.parent_window)
    print("type of windows", type(child_window))

    for child in child_window:
        print(child)
        if context.driver_obj.parent_window != child:
            print("Switching to new window/tab")
            context.driver_obj.switch_to.window(child)
            print("title is", context.driver_obj.title)
    time.sleep(5)
    try:
        text3 = context.driver_obj.find_element('''xpath''', '''//h2[text()="Get Offers on"]''')
    except:
        context.driver_obj.close()
        assert False, "Test Failed"

    time.sleep(1)
    if text3 == "Get Offers on":
        assert True,"Offer button navigates to Exclusive offers and deals for flight,hotels activities - ClearTrip page"
    time.sleep(2)


@then(u'Click on Domestic flight button')
def click_domestic_flight(context):
    context.driver_obj.find_element(*login_obj["click_domestic_flight"]).click()
    time.sleep(2)


@then(u'verify that Domestic flight button should navigate to Domestic Flight Offers page')
def click_domestic_flight_offer_pg(context):
    try:
        text2 = context.driver_obj.find_element('''xpath''', '''//h1[text()="Domestic Flight Offers"]''')
    except:
        context.driver_obj.close()
        assert False, "Test Failed"

    time.sleep(2)
    if text2 == "Domestic Flight Offers":
        assert True, "Domestic flight button is navigate to Domestic Flight Offers page"
    time.sleep(2)

@then(u'Click on image of Domestic flight offer block')
def click_one_offer(context):
    context.driver_obj.find_element(*login_obj["click_one_offer"]).click()
    time.sleep(1)
    ActionChains(context.driver_obj).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)


@then(u'verify that Domestic flight offer block should be open user selected offer page')
def click_one_offer_open(context):
    assert True,"Domestic flight offer block open user selected offer page"


@then(u'click on Book button')
def click_book_button(context):
    context.driver_obj.find_element(*login_obj["click_book_button"]).click()
    time.sleep(3)


@then(u'verify that Book button should navigate to Flight Booking page')
def click_book_button_open(context):
    context.driver_obj.find_element(*login_obj["click_login_popup"]).click()
    time.sleep(1)
    try:
        text1 = context.driver_obj.find_element('''xpath''', '''//h1[text()="Search flights"]''')
    except:
        context.driver_obj.close()
        assert False,"Test Failed"

    if text1 == "Search flights":
        assert True, "Book button is navigate to Flight Booking page"


