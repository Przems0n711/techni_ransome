import os
import sys
import msvcrt
import ctypes

def block_file_editing(file_path, user_pass):
    if user_pass == "hackermati": #pswd to block file
        try:
            attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            ctypes.windll.kernel32.SetFileAttributesW(file_path, attributes | 0x02)
            print("File editing has been blocked successfully!")
        except OSError:
            print("Failed to block file editing.")

def unblock_file_editing(file_path, user_pass):
    if user_pass == "matiszef": #pswd to unblock file
        try:
            attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            ctypes.windll.kernel32.SetFileAttributesW(file_path, attributes & ~0x02)
            print("The file has been unblocked!")
        except OSError:
            print("Failed to unblock the file.")

file_path = r"paste your selected file path" #Do not remove r" before path track!

user_pass = input("Enter the password to block the file: ")

block_file_editing(file_path, user_pass)

print("You can't do this HAHA - pay $100000 to @ogprzemo on PayPal")

user_pass = input("Enter the password to unblock the file: ")

attempt = 0
while attempt < 3:
    if user_pass == "matiszef":
        unblock_file_editing(file_path, user_pass)
        break
    else:
        attempt += 1
        print(f"Invalid password! You have {3 - attempt} attempts left.")
        user_pass = input("Enter the password to unblock the file: ")

if attempt == 3:
    print("The file will remain blocked!")

msvcrt.getch()