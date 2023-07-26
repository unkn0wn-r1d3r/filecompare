#!/bin/bash

# Prompt the user for the filenames of the two text files
read -p "Enter the filename of the first text file: " file1
read -p "Enter the filename of the second text file: " file2

# Check if the files exist
if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
  echo "Error: One or both files not found."
  exit 1
fi

# Sort both files before comparison
sort "$file1" > sorted_file1.txt
sort "$file2" > sorted_file2.txt

# Compare the two sorted files and store the unique items in a new file
comm -23 sorted_file1.txt sorted_file2.txt > unique_items.txt

# Remove temporary sorted files
rm sorted_file1.txt sorted_file2.txt

echo "Unique items saved to unique_items.txt."
