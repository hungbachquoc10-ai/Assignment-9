def caesar_cipher_file(file_name, shift, direction):
    n = shift if direction.lower() == 'right' else -shift
    ciphertext = ""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        for char in content:
            if 'A' <= char <= 'Z':
                x = ord(char)
                new_char = chr((x - 65 + n) % 26 + 65)
                ciphertext += new_char
            elif 'a' <= char <= 'z':
                x = ord(char)
                new_char = chr((x - 97 + n) % 26 + 97)
                ciphertext += new_char
            else:
                ciphertext += char
        with open("plain text", "w") as output_file:
            output_file.write(ciphertext)
        return "Ciphertext has been written to the plain text file"
    except FileNotFoundError:
        return "Error: The input file was not found."
#I will put my file path, shift number, and direction (right or left) in the line below to run the function.
print(caesar_cipher_file("#your_file_path_here#", "#your_shift_number", "#your_direction_here#"))
