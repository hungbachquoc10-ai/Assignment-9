def count_non_blank_lines(file_path):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    count += 1
    except FileNotFoundError:
        return "Error: The file was not found."
    return count
print(count_non_blank_lines("#put_your_file_path_here#")) 
