import nltk
nltk.download('punkt')
# NLTK data path
nltk.data.path.append("C:\\Users\\Vysikan\\nltk_data")
nltk.data.path.append("C:\\nltk_data")  

nltk.download('words')

from nltk.corpus import words

def decipher(input_string, the_shift_key):
    ans = ''

    for char in input_string:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + the_shift_key) % 26 + ord('A' if is_upper else 'a'))
            ans += shifted_char
        else:
            ans += char

    return ans

def is_meaningful(txt):
    english_word_set = set(words.words())

    word_tokens = nltk.word_tokenize(txt.lower())  

    meaningful_word_count = sum(1 for word in word_tokens if word in english_word_set)
    percentage_meaningful = (meaningful_word_count / len(word_tokens)) * 100

    leniency = 65  
    return percentage_meaningful >= leniency

def find_shift_key(cyphered_txt):
    cyphered_txt = cyphered_txt.upper()
    print('---Decipherment Under Function---')
    
    for shift in range(26):
        decrypted_txt = decipher(cyphered_txt, -shift)
        if is_meaningful(decrypted_txt):
            print(f'The Shift Key: {shift:2}')
            return shift

    print('Could not find the shift key')
    return None

encrypted_txt1 = """VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

print(f'Undeciphered Cryptogram: {encrypted_txt1}')
shift_key1 = find_shift_key(encrypted_txt1)
if shift_key1 is not None:
    decrypted_message1 = decipher(encrypted_txt1, -shift_key1)
    print(f"The deciphered quote is: {decrypted_message1}\n")

