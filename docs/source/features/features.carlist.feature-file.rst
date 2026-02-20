.. role:: gherkin-step-keyword
.. role:: gherkin-step-content
.. role:: gherkin-feature-description
.. role:: gherkin-scenario-description
.. role:: gherkin-feature-keyword
.. role:: gherkin-feature-content
.. role:: gherkin-background-keyword
.. role:: gherkin-background-content
.. role:: gherkin-scenario-keyword
.. role:: gherkin-scenario-content
.. role:: gherkin-scenario-outline-keyword
.. role:: gherkin-scenario-outline-content
.. role:: gherkin-examples-keyword
.. role:: gherkin-examples-content
.. role:: gherkin-tag-keyword
.. role:: gherkin-tag-content

:gherkin-feature-keyword:`Feature:` :gherkin-feature-content:`Car List API Endpoint`
====================================================================================

    :gherkin-feature-description:`As a registered user`
    :gherkin-feature-description:`I want to retrieve a list of cars`
    :gherkin-feature-description:`So that I can manage my fleet efficiently`

:gherkin-background-keyword:`Background:`
-----------------------------------------

| :gherkin-step-keyword:`Given` the following cars exist in my account\:

    .. csv-table::
        :header: "Name", "Type", "Created At"
        :quote: “

        “Blue Sedan“, “Private“, “2026-01-01“
        “Red Truck“, “Company“, “2026-01-02“
        “Silver Coupe“, “Private“, “2026-01-03“


:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`The one where there are no cars for the user`
--------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` I have an empty car collection
| :gherkin-step-keyword:`When` I request the list of cars
| :gherkin-step-keyword:`Then` I should receive an empty list

:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`The one where there is one car`
------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` I have exactly one \"Electric SUV\" in my account
| :gherkin-step-keyword:`When` I request the list of cars
| :gherkin-step-keyword:`Then` the response should contain 1 car
| :gherkin-step-keyword:`And` the car name should be \"Electric SUV\"

:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`The one where there are many cars`
---------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`When` I request the list of cars
| :gherkin-step-keyword:`Then` the response should contain 3 cars
| :gherkin-step-keyword:`And` the names should be \"Blue Sedan\", \"Red Truck\", and \"Silver Coupe\"

:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`The one where cars are sorted by creation date`
----------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`When` I request the list of cars
| :gherkin-step-keyword:`Then` the cars should be returned in the following order\:

    .. csv-table::
        :header: "Name"
        :quote: “

        “Blue Sedan“
        “Red Truck“
        “Silver Coupe“


:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Filter cars by ownership type`
-----------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`When` I request the list of cars filtered by \"**\<filter\>**\"
| :gherkin-step-keyword:`Then` the response should contain **\<count\>** cars
| :gherkin-step-keyword:`And` all returned cars should have the type \"**\<filter\>**\"

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "filter", "count"
    :quote: “

    “Private“, “2“
    “Company“, “1“

:gherkin-scenario-outline-keyword:`Scenario Outline:` :gherkin-scenario-outline-content:`Filter returns no results when types don't match`
------------------------------------------------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`Given` I only have \"**\<actual_type\>**\" cars in my account
| :gherkin-step-keyword:`When` I request the list of cars filtered by \"**\<filter_type\>**\"
| :gherkin-step-keyword:`Then` I should receive an empty list

:gherkin-examples-keyword:`Examples:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "actual_type", "filter_type"
    :quote: “

    “Private“, “Company“
    “Company“, “Private“

:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Requesting a limited set of results`
-----------------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`When` I request the list of cars with a limit of 2
| :gherkin-step-keyword:`Then` the response should contain 2 cars
| :gherkin-step-keyword:`And` the names should be \"Blue Sedan\" and \"Red Truck\"

:gherkin-scenario-keyword:`Scenario:` :gherkin-scenario-content:`Requesting an invalid filter`
----------------------------------------------------------------------------------------------

| :gherkin-step-keyword:`When` I request the list of cars filtered by \"Spacecraft\"
| :gherkin-step-keyword:`Then` the API should return a 400 Bad Request error
| :gherkin-step-keyword:`And` the message should state \"Invalid ownership type\"

