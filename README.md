# 💼 Employee Data Formatter with Google Gemini AI

This project integrates Google Gemini (Generative AI) to intelligently format dummy employee data into structured summaries.

## ✨ Features

- Randomly selects between different dummy employee data formats.
- Uses Google Gemini to generate clean, structured JSON from unstructured data.
- Extracts the employee with the highest salary and creates an enhanced descriptive summary.
- Modular and extensible code structure.

## 📁 Project Structure

```
employee-genai/
│
├── data_processing.py         # Utility functions and dummy data generation
├── main.py                    # Main script using Gemini for formatting and summarization
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## 🛠️ Requirements

- Python 3.10+
- Google Generative AI API key

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Setup

1. Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
2. Open `main.py` and replace the API key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

## 🚀 Usage

Run the project:

```bash
python main.py
```

The script will:
- Load random dummy employee data
- Format it using Gemini AI
- Output the most descriptive info about the highest-paid employee

## 📄 Example Output

```text
Name: Diana
About Employee: Diana works in Finance. With over 5 years of experience and a salary of 80000 per month, she plays a key role in managing financial operations and strategy.
```

## 📦 Dummy Data Utilities

From `data_processing.py`:
- `get_dummy_employee_data_sql()`
- `get_dummy_employee_data_json()`
- `get_dummy_employee_data_text()`

Plus helpers:
- `filter_items(items, keyword)`
- `transform_items(items)`
- `aggregate_items(items)`

## 📜 License

MIT License

## 🙌 Author

**Sakshi** – Developer & AI Explorer