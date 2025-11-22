#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Palindrome Checker"""

def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_word = "madam"
    result = is_palindrome(test_word)
    
    if result:
        print(f"'{test_word}' is a palindrome!")
    else:
        print(f"'{test_word}' is not a palindrome.")
