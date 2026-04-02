def find_keyword_lines(file_path, keyword):
    line_numbers = []
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if keyword in line:
                    line_numbers.append(line_number)        
    except FileNotFoundError:
        return "Error: The file was not found."
    return line_numbers
#I will put my file path and keyword in the line below to run the function and find the line numbers containing the keyword.
print(find_keyword_lines("#put_your_file_path_here#","#put_your_keyword_here#"))
