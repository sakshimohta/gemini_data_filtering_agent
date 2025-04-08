import pandas as pd


def filter_items(items, keyword):
    """Filter items based on a keyword in their name or description."""
    if not isinstance(items, list):
        raise ValueError("Expected 'items' to be a list of dictionaries.")
    filtered_items = []
    for item in items:
        if isinstance(item, dict):
            # Safely access 'name' and 'description' keys
            name = item.get('name', '').lower()
            description = item.get('description', '').lower()
            if keyword.lower() in name or keyword.lower() in description:
                filtered_items.append(item)
    return filtered_items

def transform_items(items):
    """Transform items by adding a new field."""
    for item in items:
        # Safely access 'name' and 'description' keys
        name = item.get('name', 'Unknown')
        description = item.get('description', 'No description')
        item['summary'] = f"{name} - {description}"
    return items

def aggregate_items(items):
    """Aggregate items to count the total number."""
    return {"total_items": len(items)}


def get_dummy_employee_data_sql():
    """Return a dummy dataframe with employee data."""
    data = {
        "EmployeeID": [1, 2, 3, 4, 5],
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Department": ["HR", "Engineering", "Marketing", "Finance", "IT"],
        "Salary": [50000, 70000, 60000, 80000, 55000],
        "JoiningDate": ["2020-01-15", "2019-03-10", "2021-06-25", "2018-11-30", "2022-07-01"],
    }
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")

def get_dummy_employee_data_json():
    """Return a dummy JSON object with employee data."""
    data = {
        "employees": [
            {"EmployeeID": 1, "Name": "Alice", "Department": "HR", "Salary": 50000, "JoiningDate": "2020-01-15"},
            {"EmployeeID": 2, "Name": "Bob", "Department": "Engineering", "Salary": 70000, "JoiningDate": "2019-03-10"},
            {"EmployeeID": 3, "Name": "Charlie", "Department": "Marketing", "Salary": 60000, "JoiningDate": "2021-06-25"},
            {"EmployeeID": 4, "Name": "Diana", "Department": "Finance", "Salary": 80000, "JoiningDate": "2018-11-30"},
            {"EmployeeID": 5, "Name": "Eve", "Department": "IT", "Salary": 55000, "JoiningDate": "2022-07-01"},
        ]
    }
    return data

def get_dummy_employee_data_text():
    """Return a dummy text representation of employee data."""
    data = """
    EmployeeID: 1, Name: Alice, Department: HR, Salary: 50000, JoiningDate: 2020-01-15
    EmployeeID: 2, Name: Bob, Department: Engineering, Salary: 70000, JoiningDate: 2019-03-10
    EmployeeID: 3, Name: Charlie, Department: Marketing, Salary: 60000, JoiningDate: 2021-06-25
    EmployeeID: 4, Name: Diana, Department: Finance, Salary: 80000, JoiningDate: 2018-11-30
    EmployeeID: 5, Name: Eve, Department: IT, Salary: 55000, JoiningDate: 2022-07-01
    """
    return data.strip()

