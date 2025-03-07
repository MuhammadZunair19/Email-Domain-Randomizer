import pandas as pd
import random
import tkinter as tk
from tkinter import filedialog

# List of random domains
random_domains = [
    "@yahoo.com", "@hotmail.com", "@outlook.com", "@aol.com", "@zoho.com",
    "@icloud.com", "@mail.com", "@yandex.com", "@protonmail.com", "@gmx.com",
    "@hotmail.de", "@yahoo.co.uk", "@t-online.de", "@rocketmail.com"
]


# Function to get a random domain
def get_random_domain():
    return random.choice(random_domains)


# Function to modify email addresses
def modify_email(email):
    if pd.isna(email) or "@" not in str(email):
        return email  # Keep invalid/missing emails unchanged

    username, domain = email.split("@", 1)  # Split at the first '@'

    if domain.lower() == "gmail.com":
        return email  # Keep Gmail unchanged
    else:
        return username + get_random_domain()  # Replace domain randomly


# Function to process the CSV file
def process_emails(input_file, output_file):
    # Read CSV file
    df = pd.read_csv(input_file)

    # Ensure the column exists
    email_column = None
    for col in df.columns:
        if "email" in col.lower():  # Detect email column (case insensitive)
            email_column = col
            break

    if not email_column:
        print("Error: No column containing 'Email' found in the CSV.")
        return

    # Apply modification
    df[email_column] = df[email_column].apply(modify_email)

    # Save the modified data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Modified emails saved to {output_file}")


# Function to prompt file upload and process it
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to upload a file
    input_file = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

    if not input_file:
        print("No file selected. Exiting.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Modified CSV"
    )

    if not output_file:
        print("No output file selected. Exiting.")
        return

    # Process the file
    process_emails(input_file, output_file)


if __name__ == "__main__":
    main()
