# Building a CSV Data Cleaner with Python, Pandas, and Tkinter

## Introduction

CSV files are widely used to store and exchange structured data, but their contents are not always consistent. Names may have different capitalization, text fields may contain unnecessary spaces, email addresses may be incorrectly formatted, and numeric values may contain invalid data.

To explore how these problems can be addressed with Python, I developed **CSV Data Cleaner**, a lightweight desktop application that automates several common data-cleaning tasks.

The application uses Python, Pandas, and Tkinter. It provides a graphical interface through which users can select a CSV file, clean its contents according to predefined rules, and save the processed data in a project-specific directory.

Most of the code was generated with AI assistance. The development process involved adapting the initial solution to new requirements, testing its behavior, and resolving a compatibility issue with newer versions of Pandas.

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

## Development Process

The project began as a beginner-level Python task: create a script that could clean a customer CSV file containing inconsistent information.

The original requirements were straightforward. The program needed to read a CSV file, remove unnecessary spaces, standardize names, convert email addresses to lowercase, remove rows with invalid or missing email addresses, and replace missing purchase amounts with zero.

### From a command-line script to a desktop application

The first implementation was a command-line script using Pandas. A sample customer dataset was created to test different situations, including extra spaces, inconsistent capitalization, invalid email formats, missing values, and purchase amounts that could not be converted to numbers.

The initial version used command-line arguments to specify the input and output filenames. During development, this approach was changed to interactive input so users could enter the file paths themselves.

Another requirement was introduced: the cleaned file should be saved automatically in the user's Downloads folder.

The project then evolved into a graphical desktop application. Tkinter was introduced to provide a file-selection dialog, an output filename field, and a button to start the cleaning process. This removed the need for users to enter file paths manually in the terminal.

### Organizing the application files

As the application became more structured, the output location was changed again.

Instead of saving files in the Downloads folder, the current version creates a `data` directory next to the Python script and saves cleaned CSV files there.

This makes the output location predictable and keeps generated files associated with the project.

### Testing and pandas compatibility

Testing the application with a newer development environment revealed a compatibility problem.

The original implementation used `DataFrame.applymap()` to remove leading and trailing spaces from string values. This method is no longer available in newer pandas versions, causing the application to display an error when the cleaning button was clicked.

The solution was to replace `DataFrame.applymap()` with `Series.map()` applied individually to each column:

```python
for column in df.columns:
    df[column] = df[column].map(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )
```

This approach cleans string values without changing non-string values and avoids relying on the removed DataFrame method.

The application was subsequently tested with Python 3.14.10 and Pandas 3.1.1 in PyCharm 2025.3.1.1.

This testing process highlighted an important part of software development: code that works in one environment may need adjustments when libraries are updated.

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

Cleaned CSV files are saved in this directory.

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
│   └── test_data.csv
├── screenshots/
│   ├── main-window.png
│   ├── selected-file.png
│   └── cleaned-result.png
├── requirements.txt
├── .gitignore
└── README.md
```

The main Python file contains the application logic. The `data` directory holds sample and generated files, while `screenshots` contains images documenting the user interface.

Generated output files can be kept local rather than committed to the repository.

## Installation and Usage

The application requires Python, Pandas, and a working Tkinter installation.

Install the dependency with:

```bash
pip install -r requirements.txt
```

Save the source code as `csv_data_cleaner.py` and run:

```bash
python csv_data_cleaner.py
```

When the application opens:

1. Select a CSV file using **Browse**.
2. Enter a name for the output file.
3. Click **Clean CSV File**.
4. Review the result message and locate the cleaned file in the project's `data` directory.

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

## AI-Assisted Development

An important part of this project is the use of AI during development.

Most of the code was generated with AI assistance. The initial implementation was gradually adapted as new requirements emerged, including interactive file selection, a graphical interface, local output storage, and compatibility with newer pandas versions.

The development process also demonstrated that AI-generated code is not automatically correct or production-ready. The `DataFrame.applymap()` compatibility issue was discovered through actual testing and required a code change.

This project illustrates a practical approach to AI-assisted programming: using AI to accelerate implementation while testing the resulting application, understanding its behavior, and improving it when problems arise.

## Conclusion

CSV Data Cleaner is a small Python desktop application that automates common CSV-cleaning operations through a straightforward graphical interface.

Its development began with a simple command-line task and evolved into a desktop application through several practical improvements.

By combining Pandas for data processing, Tkinter for user interaction, regular expressions for basic email validation, and `pathlib` for file management, the project brings several useful programming concepts together in one practical tool.

The project also demonstrates how testing and compatibility adjustments are important parts of software development, particularly when working with evolving libraries.

Most of the code was created with AI assistance, making this project an example of how AI can support software development while leaving room for testing, learning, and continuous improvement.
