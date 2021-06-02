import nltk  
import re

from nltk.util import pr

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()
import string
letters_list = list(string.ascii_lowercase) 
# print(letters_list)

def encrypt(phrase,num_shift):
    after_encrypt =""
    only_let= re.sub(r'[^A-Za-z]+',' ', phrase).lower()
    if num_shift > 26:
        num_shift= num_shift + 26
    for char in only_let:
        # print(char)
        if char in letters_list:
            corr_ind = letters_list.index(char) # why not +1
            new = letters_list[(corr_ind + num_shift) % 26] # take the one item from the list by index
            after_encrypt += new
        else: # not lose other char
            after_encrypt += char 
    # print(after_encrypt)
    return after_encrypt

         

def decrypt(encrypted,num_shift):
    return encrypt(encrypted,-num_shift)
# def decrypts(encrypted,num_shift):
#     befor_encrypt =""
#     only_let= re.sub(r'[^A-Za-z]+',' ', encrypted).lower()
#     if num_shift > 26:
#         num_shift= num_shift -28
#     for char in only_let:
#         # print(char)
#         if char in letters_list:
#             corr_ind = letters_list.index(char) # why not +1
#             new = letters_list[(corr_ind + num_shift) % 26] # take the one item from the list by index
#             befor_encrypt += new
#         else: # not lose other char
#             befor_encrypt += char 
#     print(befor_encrypt)
#     return befor_encrypt
def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count
def crack(encrypted):
    for i in range(0,26):
        text= decrypt(encrypted,i)
        percentage = int(count_words(text) / len(encrypted.split()) * 100)
        if percentage > 50:
            # print(text)
            return text 


 
print(encrypt("a",1))
print(decrypt("b",27))
# encrypt("a dark and stormy night",1)
# decrypt("b ebsl boe tupsnz ojhiu",1)
print(crack("b"))
# decrypts("b ebsl boe tupsnz ojhiu",1)

