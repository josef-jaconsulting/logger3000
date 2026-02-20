features Glossary
=================

- :term:`I have an empty car collection`
- :term:`I have exactly one \"Electric SUV\" in my account`
- :term:`I only have \"\<actual_type\>\" cars in my account`
- :term:`I request the list of cars`
- :term:`I request the list of cars filtered by \"\<filter\>\"`
- :term:`I request the list of cars filtered by \"\<filter_type\>\"`
- :term:`I request the list of cars filtered by \"Spacecraft\"`
- :term:`I request the list of cars with a limit of 2`
- :term:`I should receive an empty list`
- :term:`all returned cars should have the type \"\<filter\>\"`
- :term:`the API should return a 400 Bad Request error`
- :term:`the car name should be \"Electric SUV\"`
- :term:`the cars should be returned in the following order\:`
- :term:`the following cars exist in my account\:`
- :term:`the message should state \"Invalid ownership type\"`
- :term:`the names should be \"Blue Sedan\" and \"Red Truck\"`
- :term:`the names should be \"Blue Sedan\", \"Red Truck\", and \"Silver Coupe\"`
- :term:`the response should contain 1 car`
- :term:`the response should contain 2 cars`
- :term:`the response should contain 3 cars`
- :term:`the response should contain \<count\> cars`

.. glossary::
    I request the list of cars
        | features/carlist.feature 16, 21, 26, 32

    I should receive an empty list
        | features/carlist.feature 17, 54

    the following cars exist in my account\:
        | features/carlist.feature 7

    I have an empty car collection
        | features/carlist.feature 15

    I have exactly one \"Electric SUV\" in my account
        | features/carlist.feature 20

    the response should contain 1 car
        | features/carlist.feature 22

    the car name should be \"Electric SUV\"
        | features/carlist.feature 23

    the response should contain 3 cars
        | features/carlist.feature 27

    the names should be \"Blue Sedan\", \"Red Truck\", and \"Silver Coupe\"
        | features/carlist.feature 28

    the cars should be returned in the following order\:
        | features/carlist.feature 33

    I request the list of cars filtered by \"\<filter\>\"
        | features/carlist.feature 41

    the response should contain \<count\> cars
        | features/carlist.feature 42

    all returned cars should have the type \"\<filter\>\"
        | features/carlist.feature 43

    I only have \"\<actual_type\>\" cars in my account
        | features/carlist.feature 52

    I request the list of cars filtered by \"\<filter_type\>\"
        | features/carlist.feature 53

    I request the list of cars with a limit of 2
        | features/carlist.feature 63

    the response should contain 2 cars
        | features/carlist.feature 64

    the names should be \"Blue Sedan\" and \"Red Truck\"
        | features/carlist.feature 65

    I request the list of cars filtered by \"Spacecraft\"
        | features/carlist.feature 69

    the API should return a 400 Bad Request error
        | features/carlist.feature 70

    the message should state \"Invalid ownership type\"
        | features/carlist.feature 71

