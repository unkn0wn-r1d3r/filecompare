def read_lines(filename):
    with open(filename, 'r') as file:
        return set(file.read().splitlines())

def save_unique_items(unique_items, output_filename):
    with open(output_filename, 'w') as file:
        file.write('\n'.join(unique_items))

def compare_and_save_unique_items(file1, file2, output_filename):
    lines1 = read_lines(file1)
    lines2 = read_lines(file2)

    unique_items = lines1.symmetric_difference(lines2)

    save_unique_items(unique_items, output_filename)

if __name__ == "__main__":
    file1 = input("Enter the filename of the first text file: ")
    file2 = input("Enter the filename of the second text file: ")
    output_filename = input("Enter the filename to save unique items: ")

    compare_and_save_unique_items(file1, file2, output_filename)

    print("Unique items saved to", output_filename)
