#!/usr/bin/python3

import pyperclip
import pyautogui

GAJS_ALPHABET = {
    'Zh': 'Ž',
    'zh': 'ž',
    'Sh': 'Š',
    'sh': 'š',
    'Ch': 'Č',
    'ch': 'č',
    'Cj': 'Ć',
    'cj': 'ć',
    'Dj': 'Đ',
    'dj': 'đ'
} 
    
def main():
    pyautogui.hotkey('ctrl', 'x')

    selected_text = pyperclip.paste()

    for key in GAJS_ALPHABET.keys():
        selected_text = selected_text.replace(key, GAJS_ALPHABET[key])

    pyperclip.copy(selected_text)
    pyautogui.hotkey('ctrl', 'v')

if __name__ == '__main__':
    main()