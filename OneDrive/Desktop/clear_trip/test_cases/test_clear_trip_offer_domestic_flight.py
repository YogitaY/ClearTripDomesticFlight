
from POM.clear_trip_offer_domestic_flight import Offerpage

class TestOfferDFPage:
    def test_offer_domestic_flight(self,_driver):
        lp1 = Offerpage(_driver)
        lp1.click_login()
        lp1.click_offers()
        lp1.window_alter()
        lp1.click_domestic_flight()
        lp1.click_one_offer()
        lp1.click_book_button()

    # def test_offerDF(self,_driver):
    #     lp2 = Offerpage(_driver)
    #     lp2.click_login()
    #     lp2.click_offers()
    #     lp2.window_alter()
    #     lp2.click_domestic_flight()
    #     lp2.click_white_space()
    #     lp2.click_book_button()









