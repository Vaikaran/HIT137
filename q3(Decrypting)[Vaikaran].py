total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i + j 

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

# The given Encrypted code
encrypted_text = '''tybony_inevnoyr
100
zl_qvpg= {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
    tybony tybony_inevnoyr ybpny inevnoyr - 5
    ahzoref= [1, 2, 3, 4, 5]
    juvyr ybpny_inevnoyr > 0:
        vs ybpny inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny inevnoyr -= 1
    erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg = cebprff_ahzoref(ahzoref=zl_frg)
qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr
    zbqvsl_qvpg(5)
qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony inevnoyr + 10
    sbe v va enatr(5):
        cevag(v)
        V += 1
    vs zl_frg vf abg Abar naq z1_qvpg['xr14'] == 10: cevag("Pbaqvgvba zrg!")
    vs 5 abg va z1_qvpg:
        cevag("5 abg sbhaq va gur qvpgvbanel!")
        cevag(tybony_inevnoyr)
        cevag(z1_qvpg)
        cevag(z1_frg)'''


# Encryption
def encrypt(text, key): 
    encrypted_text = ""
    for char in text: 
        if char.isalpha():
            shifted = ord(char) + key 
            if char.islower():
                if shifted > ord('z'): 
                    shifted -= 26
                elif shifted < ord('a'): 
                    shifted + 26
            elif char.isupper():
                if shifted > ord('Z'): 
                    shifted -= 26
            elif shifted < ord('A'):
                shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Decrypt method
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = total
decrypted_code = decrypt(encrypted_text, key)
print(f'Key: {key}')
print('Decrypted code: ')
print(decrypted_code)