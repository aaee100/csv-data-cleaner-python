
# Building a CSV Data Cleaner with Python and AI Assistance

## Introduction

CSV files are widely used to store and exchange structured data, but their contents are not always consistent. Names may have different capitalization, text fields may contain unnecessary spaces, email addresses may be incorrectly formatted, and numeric values may contain invalid data.

To explore how these problems can be addressed with Python, I developed **CSV Data Cleaner**, a lightweight desktop application that automates several common data-cleaning tasks.

The application uses Python, Pandas, and Tkinter. It provides a graphical interface through which users can select a CSV file, clean its contents according to predefined rules, and save the processed data in a project-specific directory.

**Most of the code was generated with AI assistance.** The project demonstrates how AI can help with application development while providing an opportunity to examine the generated code, understand its structure, and identify areas for future improvement.

## Project Overview

CSV Data Cleaner is designed to make basic data preparation accessible without requiring users to write Python code themselves.

Its main features include:

- Removing leading and trailing whitespace from text values.
- Standardizing name capitalization.
- Converting email addresses to lowercase.
- Filtering out rows containing missing or incorrectly formatted email addresses.
- Converting purchase amounts to numeric values.
- Replacing invalid or missing purchase amounts with zero.
- Saving the cleaned data as a new CSV file.
- Displaying a summary of the cleaning operation.

The application recognizes three specific column names: `name`, `email`, and `purchase_amount`. The corresponding cleaning rules are applied only when those columns exist.

This makes the program suitable for simple, structured datasets that follow the expected column conventions.

## Technologies Used

### Python

Python handles the application's logic, file operations, data transformations, validation, and graphical interface.

### Pandas

Pandas provides the main data-processing functionality. It reads CSV files into DataFrames, transforms column values, filters rows, converts data types, and writes the resulting data back to CSV format.

### Tkinter

Tkinter is used to build the desktop interface. It provides the application window, text fields, buttons, file-selection dialog, and message boxes.

### Regular Expressions

The `re` module performs a basic email-format check using a regular expression.

This helps identify common formatting errors, but it does not verify whether an email address exists or can receive messages.

### pathlib

The `pathlib` module handles filesystem paths. The application uses it to locate its own directory, create a `data` folder when necessary, and construct the output file path.

## How the Application Works

The program is organized into several functions, each responsible for a specific part of the workflow.

### 1. File and Directory Setup

At startup, the program determines the directory containing the Python script using `Path(__file__).parent`.

It then creates a `data` directory if one does not already exist.

Cleaned CSV files are saved in this directory. Keeping generated files alongside the project makes the output location predictable and helps keep the project organized.

### 2. Email Validation

The `is_valid_email()` function checks whether an email value is missing and, if not, compares its string representation against a regular expression.

The check is intentionally simple. It identifies many common formatting problems but is not a complete implementation of email-address validation.

### 3. CSV Cleaning

The `clean_csv()` function performs the main data-processing operations.

First, Pandas reads the selected file into a DataFrame. The program then removes leading and trailing whitespace from string values throughout the dataset.

If a `name` column exists, its values are converted to title case. If an `email` column exists, its values are converted to lowercase, and rows with missing or invalid email formats are removed.

The function also checks for a `purchase_amount` column. If present, its values are converted to numeric data. Values that cannot be converted are replaced with zero.

Finally, the cleaned DataFrame is saved as a CSV file in the project's `data` directory. The original DataFrame index is excluded from the output.

### 4. Graphical User Interface

The application window provides three main controls:

- **Browse:** Opens a file dialog so the user can select a CSV file.
- **Output filename:** Allows the user to enter the name of the cleaned file.
- **Clean CSV File:** Starts the cleaning process.

Before processing begins, the program checks that the selected input file exists and that an output filename has been entered. If the filename does not end in `.csv`, the extension is added automatically.

The interface is intentionally simple, keeping the main workflow accessible to users who are unfamiliar with programming.

### 5. Results and Error Messages

After successful processing, the application displays a summary containing the original row count, the number of rows removed for invalid email formats, and the final number of rows saved.

If an exception occurs, an error dialog displays the corresponding error message.

This provides immediate feedback without requiring users to inspect the program's source code or terminal output.

## Project Structure

The project uses a straightforward directory layout:

```text
csv-data-cleaner-python/
├── csv_data_cleaner.py
├── data/
│   ├── test_data.csv
│   └── cleaned_data.csv
├── screenshots/
│   ├── main-window.png
│   ├── selected-file.png
│   └── cleaned-result.png
├── requirements.txt
├── .gitignore
├── README.md
└── project-writeup.md
```

The main Python file contains the application logic. The `data` directory holds sample and generated files, while `screenshots` can contain images documenting the user interface.

The `requirements.txt` file records the project's external dependencies, and the README explains installation, usage, and project features.

## Installation and Usage

The application requires Python, Pandas, and a working Tkinter installation.

Install Pandas with:

```bash
pip install pandas
```

Save the source code as `csv_data_cleaner.py` and run:

```bash
python csv_data_cleaner.py
```

When the application opens:

1. Select a CSV file using **Browse**.
2. Enter a name for the output file.
3. Click **Clean CSV File**.
4. Review the result message and locate the cleaned file in the `data` directory.

The program is intended for CSV files whose structure is compatible with the predefined cleaning rules.

## Limitations and Future Improvements

Although CSV Data Cleaner automates several useful operations, it is a small utility rather than a comprehensive data-quality platform.

### More flexible column handling

The current implementation recognizes specific column names. Future versions could let users choose columns manually or configure cleaning rules through the interface.

### Improved data validation

The email validator checks formatting rather than actual deliverability. More detailed validation and clearer reporting could help users identify questionable records without automatically discarding them.

### Safer handling of numeric values

Invalid purchase amounts are currently replaced with zero. This is convenient for some datasets, but it can also misrepresent missing or malformed values. A future version could preserve missing values or let users choose how they should be handled.

### File-overwrite protection

The application could check whether the requested output file already exists and ask for confirmation before replacing it.

### Additional functionality

Other possible improvements include duplicate-row detection, support for Excel files, a preview of the cleaned data, configurable cleaning rules, and more detailed statistics about the changes made.

These improvements would make the application more flexible and suitable for a wider range of real-world datasets.

## AI-Assisted Development

An important part of this project is the use of AI during development.

Most of the code was generated with AI assistance, helping to produce an initial implementation of the data-processing functions, file handling, and graphical interface.

However, AI-generated code is not automatically correct or production-ready. Its behavior still needs to be understood and tested, particularly when handling malformed input, unexpected data types, and files containing information that must not be lost.

This project illustrates a practical approach to AI-assisted programming: using AI to accelerate implementation while treating the resulting code as something that must be evaluated and improved.

## Conclusion

CSV Data Cleaner is a small Python desktop application that automates common CSV-cleaning operations through a straightforward graphical interface.

By combining Pandas for data processing, Tkinter for user interaction, regular expressions for basic email validation, and `pathlib` for file management, the project brings several useful programming concepts together in one practical tool.

The project also provides a foundation for further development, including more flexible validation, safer file handling, and configurable cleaning operations.

Most of the code was created with AI assistance, making this project an example of how AI can support software development while leaving room for testing, learning, and continuous improvement.
