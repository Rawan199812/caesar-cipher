from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_a_string_with_shift():
    actual= encrypt('a dark and stormy night',1)
    expected ='b ebsl boe tupsnz ojhiu'
    assert actual==expected
def test_decrypt_a_previously_encrypted_string_with_the_same_shift():
    pass
def test_encryption_should_handle_upper_and_lower_case_letters():
    pass
# def test_encryption should allow non-alpha characters but ignore them, including white space
# def test_decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.