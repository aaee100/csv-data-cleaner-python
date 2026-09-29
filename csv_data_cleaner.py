import pandas as pd
import re
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


# -------------------------
# File setup
# -------------------------
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)


# -------------------------
# Email validation
# -------------------------
def is_valid_email(email):
    """Check if an email address has a valid format."""
    if pd.isna(email):
        return False

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, str(email).strip()) is not None


# -------------------------
# Clean CSV file
# -------------------------
def clean_csv(input_file, output_filename):
    try:
        # Read CSV file
        df = pd.read_csv(input_file)

        # Strip spaces from all string columns
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Fix name capitalization
        if 'name' in df.columns:
            df['name'] = df['name'].str.title()

        # Lowercase all emails
        if 'email' in df.columns:
            df['email'] = df['email'].str.lower()

            # Remove invalid or missing emails
            before_rows = len(df)
            df = df[df['email'].apply(is_valid_email)]
            removed = before_rows - len(df)
        else:
            before_rows = len(df)
            removed = 0

        # Clean purchase amounts
        if 'purchase_amount' in df.columns:
            df['purchase_amount'] = pd.to_numeric(
                df['purchase_amount'],
                errors='coerce'
            ).fillna(0)

        # Save cleaned file inside data folder
        output_path = DATA_DIR / output_filename
        df.to_csv(output_path, index=False)

        messagebox.showinfo(
            "Success",
            f"Cleaned data saved to:\n{output_path}\n\n"
            f"Summary:\n"
            f" - Total rows before cleaning: {before_rows}\n"
            f" - Invalid email rows removed: {removed}\n"
            f" - Final rows saved: {len(df)}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"An error occurred:\n{e}"
        )


# -------------------------
# Select input file
# -------------------------
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)


# -------------------------
# Start cleaning
# -------------------------
def start_cleaning():
    input_file = entry_file_path.get().strip()
    output_filename = entry_output_name.get().strip()

    if not input_file or not Path(input_file).is_file():
        messagebox.showerror(
            "Error",
            "Please select a valid CSV file."
        )
        return

    if not output_filename:
        messagebox.showerror(
            "Error",
            "Please enter a name for the cleaned file."
        )
        return

    if not output_filename.lower().endswith(".csv"):
        output_filename += ".csv"

    clean_csv(input_file, output_filename)


# -------------------------
# GUI Setup
# -------------------------
root = tk.Tk()
root.title("CSV Data Cleaner")
root.geometry("500x250")
root.resizable(False, False)


# File selection
tk.Label(
    root,
    text="Select CSV file to clean:",
    font=("Arial", 11)
).pack(pady=5)

frame_file = tk.Frame(root)
frame_file.pack()

entry_file_path = tk.Entry(
    frame_file,
    width=50
)
entry_file_path.pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_file,
    text="Browse",
    command=select_file
).pack(side=tk.LEFT)


# Output name
tk.Label(
    root,
    text="Enter output file name (e.g. cleaned_data.csv):",
    font=("Arial", 11)
).pack(pady=10)

entry_output_name = tk.Entry(
    root,
    width=40
)
entry_output_name.pack()


# Clean button
tk.Button(
    root,
    text="Clean CSV File",
    command=start_cleaning,
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=20)


root.mainloop()