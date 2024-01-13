import os
import pandas as pd
from collections import Counter

# Obtain user's directory
home_dir = os.path.expanduser("~")

# Construct path to txt file in Downloads directory
txt_file_path = os.path.join(home_dir, "Downloads", "Combined_Text.txt")

# Read contents of txt file
with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

# Tokenize the text into words
words = txt_content.split()

# Record occurrences of each word
word_counts = Counter(words)

# Formulate top 30 most common words
top_30_words = word_counts.most_common(30)

# Create a DataFrame from the top 30 words and corresponding counts
df_top_30 = pd.DataFrame(top_30_words, columns=['Word', 'Count'])

# Path to the CSV file
csv_file_path = os.path.join(home_dir, "Downloads", "Top_30_Words_Count.csv")

# Save  DataFrame to CSV file
df_top_30.to_csv(csv_file_path, index=False)

print("Top 30 common words and their counts exported to:", csv_file_path)
