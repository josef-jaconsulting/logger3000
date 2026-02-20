Feature: Car List API Endpoint
  As a registered user
  I want to retrieve a list of cars
  So that I can manage my fleet efficiently

  Background:
    Given the following cars exist in my account:
      | Name         | Type    | Created At |
      | Blue Sedan   | Private | 2026-01-01 |
      | Red Truck    | Company | 2026-01-02 |
      | Silver Coupe | Private | 2026-01-03 |
  # Rule: Return List

  Scenario: The one where there are no cars for the user
    Given I have an empty car collection
    When I request the list of cars
    Then I should receive an empty list

  Scenario: The one where there is one car
    Given I have exactly one "Electric SUV" in my account
    When I request the list of cars
    Then the response should contain 1 car
    And the car name should be "Electric SUV"

  Scenario: The one where there are many cars
    When I request the list of cars
    Then the response should contain 3 cars
    And the names should be "Blue Sedan", "Red Truck", and "Silver Coupe"
  # Rule: Sort by Creation Date (Default: Ascending)

  Scenario: The one where cars are sorted by creation date
    When I request the list of cars
    Then the cars should be returned in the following order:
      | Name         |
      | Blue Sedan   |
      | Red Truck    |
      | Silver Coupe |
  # Rule: Filter for Private/Company

  Scenario Outline: Filter cars by ownership type
    When I request the list of cars filtered by "<filter>"
    Then the response should contain <count> cars
    And all returned cars should have the type "<filter>"

    Examples:
      | filter  | count |
      | Private |     2 |
      | Company |     1 |
  # Rule: Handling Mismatched Filters

  Scenario Outline: Filter returns no results when types don't match
    Given I only have "<actual_type>" cars in my account
    When I request the list of cars filtered by "<filter_type>"
    Then I should receive an empty list

    Examples:
      | actual_type | filter_type |
      | Private     | Company     |
      | Company     | Private     |
  # Rule: Pagination and Limits (Bonus)

  Scenario: Requesting a limited set of results
    When I request the list of cars with a limit of 2
    Then the response should contain 2 cars
    And the names should be "Blue Sedan" and "Red Truck"
  # Rule: Error Handling

  Scenario: Requesting an invalid filter
    When I request the list of cars filtered by "Spacecraft"
    Then the API should return a 400 Bad Request error
    And the message should state "Invalid ownership type"
