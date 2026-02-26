import requests
import uuid
import datetime
from behave import given, when, then, use_step_matcher
import logging

use_step_matcher("re")

# Helper to execute DB queries if connected
def execute_sql(context, query, params=None):
    if hasattr(context, 'db_conn') and context.db_conn:
        with context.db_conn.cursor() as cur:
            cur.execute(query, params)
        context.db_conn.commit()
    else:
        logging.warning("No DB connection to execute SQL")

@given(r'the following cars exist in my account:')
@given(r'I have the following cars in my account:')
def step_impl(context):
    if context.table:
        # Assuming user_id exists for the auth token 'test-token'
        test_user_id = 'test-user-123' 
        for row in context.table:
            car_id = str(uuid.uuid4())
            name = row['Name']
            car_type = row['Type']
            created_at = row['Created At']
            
            # This requires a 'cars' table defined with 'id', 'name', 'type', 'created_at', 'user_id'
            query = """
                INSERT INTO cars (id, name, type, "createdAt", "userId") 
                VALUES (%s, %s, %s, %s, %s)
            """
            execute_sql(context, query, (car_id, name, car_type, f"{created_at}T00:00:00Z", test_user_id))

@given(r'I have an empty car collection')
def step_impl(context):
    query = "DELETE FROM cars"
    execute_sql(context, query)

@when(r'I request the list of cars')
def step_impl(context):
    url = f"{context.base_url}/cars"
    context.response = requests.get(url, headers=context.headers)

@then(r'I should receive an empty list')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"
    data = context.response.json().get('data', [])
    assert len(data) == 0, f"Expected empty list, got {len(data)} items"

@given(r'I have exactly one "(?P<car_name>.+)" in my account')
def step_impl(context, car_name):
    # Clear background data
    query = "DELETE FROM cars"
    execute_sql(context, query)
    
    car_id = str(uuid.uuid4())
    # Assign a default type Private and today's date
    query = """
        INSERT INTO cars (id, name, type, "createdAt", "userId") 
        VALUES (%s, %s, %s, %s, %s)
    """
    execute_sql(context, query, (car_id, car_name, "Private", datetime.datetime.now().isoformat(), "test-user-123"))

@then(r'the response should contain (?P<count>\d+) car(?:s)?')
def step_impl(context, count):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"
    data = context.response.json().get('data', [])
    assert len(data) == int(count), f"Expected {count} cars, got {len(data)} items"

@then(r'the car name should be "(?P<car_name>.+)"')
def step_impl(context, car_name):
    data = context.response.json().get('data', [])
    assert data[0]['name'] == car_name, f"Expected {car_name}, got {data[0]['name']} instead"

@then(r'the names should be "(?P<name1>.+)", "(?P<name2>.+)", and "(?P<name3>.+)"')
def step_impl(context, name1, name2, name3):
    data = context.response.json().get('data', [])
    names = [car['name'] for car in data]
    expected_names = [name1, name2, name3]
    for expected in expected_names:
        assert expected in names, f"Expected {expected} to be in response, but got {names}"

@then(r'the cars should be returned in the following order:')
def step_impl(context):
    data = context.response.json().get('data', [])
    if context.table:
        for index, row in enumerate(context.table):
            expected_name = row['Name']
            actual_name = data[index]['name']
            assert actual_name == expected_name, f"Expected {expected_name} at index {index}, got {actual_name}"

@when(r'I request the list of cars filtered by "(?P<filter_type>.+)"')
def step_impl(context, filter_type):
    url = f"{context.base_url}/cars?filter_type={filter_type}"
    context.response = requests.get(url, headers=context.headers)

@then(r'all returned cars should have the type "(?P<filter_type>.+)"')
def step_impl(context, filter_type):
    data = context.response.json().get('data', [])
    for car in data:
        assert car['type'] == filter_type, f"Expected {filter_type}, got {car['type']}"

@given(r'I only have "(?P<actual_type>.+)" cars in my account')
def step_impl(context, actual_type):
    # clear existing
    query = "DELETE FROM cars"
    execute_sql(context, query)
    
    # Insert two cars of actual_type
    for i in range(2):
        car_id = str(uuid.uuid4())
        query = """
            INSERT INTO cars (id, name, type, "createdAt", "userId") 
            VALUES (%s, %s, %s, %s, %s)
        """
        execute_sql(context, query, (car_id, f"{actual_type} Car {i}", actual_type, datetime.datetime.now().isoformat(), "test-user-123"))

@when(r'I request the list of cars with a limit of (?P<limit>\d+)')
def step_impl(context, limit):
    url = f"{context.base_url}/cars?limit={limit}"
    context.response = requests.get(url, headers=context.headers)

@then(r'the names should be "(?P<name1>.+)" and "(?P<name2>.+)"')
def step_impl(context, name1, name2):
    data = context.response.json().get('data', [])
    names = [car['name'] for car in data]
    assert name1 in names, f"Missing {name1}"
    assert name2 in names, f"Missing {name2}"

@then(r'the API should return a (?P<status_code>\d+) Bad Request error')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected {status_code}, got {context.response.status_code}"

@then(r'the message should state "(?P<message>.+)"')
def step_impl(context, message):
    resp_msg = context.response.json().get('message')
    # Can be array (class-validator) or string
    if isinstance(resp_msg, list):
        assert any(message in m for m in resp_msg), f"Expected '{message}' in {resp_msg}"
    else:
        assert message in resp_msg, f"Expected '{message}', got {resp_msg}"
