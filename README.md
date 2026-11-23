
# 🧹 CSV Data Cleaner (Python + Tkinter)

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange)

## About the Project

CSV Data Cleaner is a desktop application built with **Python**, **Tkinter**, and **Pandas** for cleaning and standardizing CSV files.

The application removes unnecessary spaces, standardizes names and email addresses, removes rows with invalid or missing email addresses, and converts invalid purchase amounts to zero.

Cleaned data is saved as a new CSV file in the project's local `data` directory.

## Screenshots

### Main Window

![Main Window](screenshots/main-window.png)

## Features

- Select a CSV file using a file browser.
- Remove unnecessary spaces from text fields.
- Standardize name capitalization.
- Convert email addresses to lowercase.
- Validate email addresses using regular expressions.
- Remove rows with invalid or missing emails.
- Convert purchase amounts to numeric values.
- Replace invalid purchase amounts with `0`.
- Save cleaned data as a new CSV file.
- Display a cleaning summary after processing.
- Store test and output files locally.
- Use pandas `Series.map()` for compatibility with newer pandas versions.

## Technologies Used

- Python 3.14.10 (tested)
- Tkinter
- Pandas 3.1.1 (tested)
- Regular Expressions (`re`)
- pathlib

## Requirements

- Python 3
- Pandas
- Tkinter

Install the required package:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
csv-data-cleaner-python/
├── csv_data_cleaner.py
├── data/
│   └── test_data.csv
├── screenshots/
│   ├── main-window.png
│   ├── selected-file.png
│   └── cleaned-result.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone this repository.
2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python csv_data_cleaner.py
```

4. Select a CSV file.
5. Enter the desired output filename.
6. Click **Clean CSV File**.

The cleaned file will be saved in the project's `data` directory.

## Test Data

A sample `test_data.csv` file is included in the `data/` folder.

The test data contains examples of:

- Extra spaces
- Different name capitalization
- Uppercase email addresses
- Invalid email addresses
- Missing email addresses
- Invalid purchase amounts
- Valid purchase amounts

This allows the cleaning functionality to be tested easily.

## How It Works

The application:

1. Reads the selected CSV file using Pandas.
2. Removes leading and trailing spaces from string values.
3. Standardizes name capitalization.
4. Converts email addresses to lowercase.
5. Removes rows with invalid or missing email addresses.
6. Converts purchase amounts to numeric values.
7. Replaces invalid purchase amounts with `0`.
8. Saves the cleaned CSV file in the local `data` directory.
9. Displays a summary of the cleaning operation.

## Compatibility

The original implementation used `DataFrame.applymap()` to clean string values. This method is unavailable in newer pandas versions.

The application now uses `Series.map()` on individual columns instead.

The updated version was tested with:

- Python 3.14.10
- PyCharm 2025.3.1.1
- Pandas 3.1.1

## Article

Read more about the development process, implementation, and technical decisions:

[Building a CSV Data Cleaner with Python, Pandas, and Tkinter](article.md)

## Future Improvements

- Support additional CSV cleaning rules.
- Detect duplicate rows.
- Allow users to select which columns to clean.
- Add a preview of the cleaned data before saving.
- Add support for Excel files.
- Add more detailed cleaning statistics.
- Add dark mode interface.
