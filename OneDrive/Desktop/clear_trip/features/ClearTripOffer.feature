Feature: Clear Trip Offer

    Background: common steps
        Given launch chrome browser
        When enter clear trip url
        And Click on Offer button

    Scenario: Verification of Offer Domestic flight
        Then verify that Offer button should navigate to Exclusive offers and deals for flight,hotels activities - ClearTrip page
        And Click on Domestic flight button
        And verify that Domestic flight button should navigate to Domestic Flight Offers page
        And Click on image of Domestic flight offer block
        And verify that Domestic flight offer block should be open user selected offer page
        And click on Book button
        And verify that Book button should navigate to Flight Booking page