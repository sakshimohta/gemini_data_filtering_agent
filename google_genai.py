from google import genai
import json
import random
import pandas as pd
from data_processing import (get_dummy_employee_data_sql, get_dummy_employee_data_json,
                            get_dummy_employee_data_text)


def main():
    """Directly test and print outputs from specific functions."""
    try:

        client = genai.Client(api_key="AIzaSyDElOEWRYQZObsWhQMDUAcNFqoGX7Qwils")

        functions = [get_dummy_employee_data_sql, get_dummy_employee_data_json, get_dummy_employee_data_text]
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

        result = str(result)  
        prompt = f"""Convert the following employee data into a properly formatted JSON structure without adding extra information:
                 {result}"""

        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt,
        )
        
        # print("Response from Gemini API:", response.text)  
        
        final_result = response.text
        result = str(final_result)  
        prompt = f"""
Convert the following employee information into a structured JSON format without adding extra details:
Name: Sakshi
About Employee: Sakshi works in IT, She has been with the firm for 4 years ans is currently earning 1.2 Lakhs per month.

Ensure:
- The JSON structure is accurate and correctly formatted.
- Numeric values are properly represented.
- No additional information is added.

Return only the JSON output. {final_result}"""

        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt,
        )
        
        print("Response from Gemini API:", response.text)  



    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
    except KeyError as ke:
        print(f"KeyError occurred: {ke}")
    except TypeError as te:
        print(f"TypeError occurred: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()