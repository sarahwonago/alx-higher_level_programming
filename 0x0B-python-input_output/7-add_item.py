#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""
import sys
from os import path
from json import load, dump

FILE_NAME = "add_item.json"

def load_items(file_name):
    try:
        with open(file_name, 'r') as file:
            return load(file)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error loading file '{file_name}': {e}")
        return []

def save_items(items, file_name):
    with open(file_name, 'w') as file:
        dump(items, file)

def main():
    existing_items = load_items(FILE_NAME)
    new_items = sys.argv[1:]
    all_items = existing_items + new_items
    save_items(all_items, FILE_NAME)

if __name__ == "__main__":
    main()
