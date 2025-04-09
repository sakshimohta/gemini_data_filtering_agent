import google.generativeai as genai
import json
import random
import pandas as pd
from data_processing import (
    get_dummy_employee_data_sql,
    get_dummy_employee_data_json,
    get_dummy_employee_data_text
)

def main():
    """Directly test and print outputs from specific functions."""
    try:
        genai.configure(api_key="API_KEY_Placeholder")
        model = genai.GenerativeModel("gemini-1.5-flash")

        functions = [
            get_dummy_employee_data_sql,
            get_dummy_employee_data_json,
            get_dummy_employee_data_text
        ]
        selected_function = random.choice(functions)
        print(f"Testing {selected_function.__name__}:")

        result = selected_function()
        if isinstance(result, list):
            result = json.dumps(result, indent=2)
        elif isinstance(result, pd.DataFrame):
            result = result.to_json(orient="records")
        elif isinstance(result, dict):
            result = json.dumps(result, indent=2)
        elif isinstance(result, str):
            try:
                json.loads(result)  
            except json.JSONDecodeError:
                result = json.dumps({"text": result})
        else:
            raise TypeError(f"Unexpected return type from {selected_function.__name__}: {type(result)}")

        prompt = f"""Convert the following employee data into a properly formatted JSON structure without adding extra information:
{result}"""

        initial_response = model.generate_content(prompt)
        final_result = initial_response.text.strip()

        prompt = f"""
You are provided with an unstructured employee description.

Your task is to extract the key information and present it in a simplified, readable format.

Instructions:
- Avoid using any symbols like quotation marks or brackets.
- Use a clean key-value style with a colon and space, one field per line.
- Only include explicitly mentioned data. Do not infer or guess missing values.
- Represent numeric values correctly (e.g., experience as an integer, salary as a float with units if given).
- Do not wrap the output in JSON or code blocks.
- only include the name and about employee in the output.
- Only pick the EmployeeID where the Salary his highest.
- Show Employee salary aswell.
- Make the 'About Employee' section more descriptive and engaging, read all values associated with the said employee to enhance the result.
- Use the following format for the output:


Sample Output:
Name: Employee_A  
About Employee: Employee_A works in IT. She has been with the firm for 4 years and is currently earning 20000 per month.

Input:
{final_result}
"""


        final_response = model.generate_content(prompt)
        print("Response from Gemini API:\n", final_response.text)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
