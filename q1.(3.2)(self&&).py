from collections import Counter
from transformers import AutoTokenizer
import os

def count_and_get_top_tokens(model_name, file_path, segment_size=9000, top_tn=30):
    # Load tokenizer and initialize count
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    entire_unique_tokens = set()

    # Process segment files
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            segment = file.read(segment_size)
            if not segment:
                break  # End 

            # Tokenize segment
            print('Reading batch...')
            tokens = tokenizer.tokenize(segment)

            # Update entire unique tokens
            entire_unique_tokens.update(set(tokens))

    # Get the top N unique tokens
    top_unique_tokens = Counter(entire_unique_tokens).most_common(top_tn)
    return top_unique_tokens

def write_to_file(file_path, top_tokens):
    # Form txt file
    open(file_path, "w").close()
    print("Document currently processing...")
    for index, (token, count) in enumerate(top_tokens):
        token_str = f"Token {(index + 1)}: {token}"
        print(token_str)
        with open(file_path, 'a') as the_file:
            the_file.writelines(token_str + '\n')

    print('Done')

# User's directory
home_dir = os.path.expanduser("~")

# Construct paths to text file and output file in Downloads directory
READ_FILE_PATH = os.path.join(home_dir, "Downloads", "Combined_Text.txt")
WRITE_FILE_PATH = os.path.join(home_dir, "Downloads", "top30Tokens_Q1_T3_02.txt")

# Pre-trained model name
MODEL_NAME = 'bert-base-uncased'

# Number unique tokens in 'Combined_Text.txt'
top_unique_tokens = count_and_get_top_tokens(MODEL_NAME, READ_FILE_PATH)

write_to_file(WRITE_FILE_PATH, top_unique_tokens)
