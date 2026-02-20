from behave import given, when, then, use_step_matcher
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use regex matcher for better IDE compatibility
use_step_matcher("re")

@given(r'the following cars exist in my account:')
def step_impl(context):
    logger.info("Executing Step: Given the following cars exist in my account:")
    if context.table:
        for row in context.table:
            logger.info(f"  Car: {row['Name']}, Type: {row['Type']}, Created At: {row['Created At']}")

@given(r'I have an empty car collection')
def step_impl(context):
    logger.info("Executing Step: Given I have an empty car collection")

@when(r'I request the list of cars')
def step_impl(context):
    logger.info("Executing Step: When I request the list of cars")

@then(r'I should receive an empty list')
def step_impl(context):
    logger.info("Executing Step: Then I should receive an empty list")

@given(r'I have exactly one "(?P<car_name>.+)" in my account')
def step_impl(context, car_name):
    logger.info(f"Executing Step: Given I have exactly one \"{car_name}\" in my account")

@then(r'the response should contain (?P<count>\d+) car')
def step_impl(context, count):
    logger.info(f"Executing Step: Then the response should contain {count} car")

@then(r'the response should contain (?P<count>\d+) cars')
def step_impl(context, count):
    logger.info(f"Executing Step: Then the response should contain {count} cars")

@then(r'the car name should be "(?P<car_name>.+)"')
def step_impl(context, car_name):
    logger.info(f"Executing Step: And the car name should be \"{car_name}\"")

@then(r'the names should be "(?P<name1>.+)", "(?P<name2>.+)", and "(?P<name3>.+)"')
def step_impl(context, name1, name2, name3):
    logger.info(f"Executing Step: And the names should be \"{name1}\", \"{name2}\", and \"{name3}\"")

@then(r'the cars should be returned in the following order:')
def step_impl(context):
    logger.info("Executing Step: Then the cars should be returned in the following order:")
    if context.table:
        for row in context.table:
            logger.info(f"  Expected: {row['Name']}")

@when(r'I request the list of cars filtered by "(?P<filter>.+)"')
def step_impl(context, filter):
    logger.info(f"Executing Step: When I request the list of cars filtered by \"{filter}\"")

@then(r'all returned cars should have the type "(?P<filter>.+)"')
def step_impl(context, filter):
    logger.info(f"Executing Step: And all returned cars should have the type \"{filter}\"")

@given(r'I only have "(?P<actual_type>.+)" cars in my account')
def step_impl(context, actual_type):
    logger.info(f"Executing Step: Given I only have \"{actual_type}\" cars in my account")

@when(r'I request the list of cars with a limit of (?P<limit>\d+)')
def step_impl(context, limit):
    logger.info(f"Executing Step: When I request the list of cars with a limit of {limit}")

@then(r'the names should be "(?P<name1>.+)" and "(?P<name2>.+)"')
def step_impl(context, name1, name2):
    logger.info(f"Executing Step: And the names should be \"{name1}\" and \"{name2}\"")

@then(r'the API should return a 400 Bad Request error')
def step_impl(context):
    logger.info("Executing Step: Then the API should return a 400 Bad Request error")

@then(r'the message should state "(?P<message>.+)"')
def step_impl(context, message):
    logger.info(f"Executing Step: And the message should state \"{message}\"")
