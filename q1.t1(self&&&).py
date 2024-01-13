import os
import pandas as pd
import zipfile
import io

# Get the user's home directory
home_dir = os.path.expanduser("~")

# Construct the path to the zipped folder in the Downloads directory
zip_folder = "Downloads"
zip_file_name = "Assignment 2.zip"
zip_path = os.path.join(home_dir, zip_folder, zip_file_name)

every_txts = []

# Open the zip file and iterate through CSV files
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for file_name in zip_ref.namelist():
        if file_name.endswith(".csv"):
            # Read the CSV file directly from the zip archive
            with zip_ref.open(file_name) as file:
                df = pd.read_csv(io.TextIOWrapper(file))

                # Extract the 'TEXT' or 'SHORT-TEXT' column and append to the list
                if 'TEXT' in df.columns:
                    every_txts.extend(df['TEXT'].astype(str))
                elif 'SHORT-TEXT' in df.columns:
                    every_txts.extend(df['SHORT-TEXT'].astype(str))

# Put all the texts into a single string
consolidated_txt = '\n'.join(every_txts)

# Path to the output text file
outward_txt_file = os.path.join(home_dir, zip_folder, "Combined_Text.txt")

# Publish the text file
with open(outward_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write(consolidated_txt)

print("Texts exported and pasted to:", outward_txt_file)
