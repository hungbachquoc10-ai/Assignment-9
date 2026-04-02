def calculate_average_score(file_path):
    total_score = 0
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) == 2:
                    try:
                        score = float(parts[1]) 
                        total_score += score
                        count += 1
                    except ValueError:
                        print(f"Skipping line with invalid score: {line}")
        if count == 0:
            return 0.0
        return total_score / count
    except FileNotFoundError:
        return "Error: The file was not found."
#I will put my file path in the line below to run the function and calculate the average score.
avg = calculate_average_score("#put_your_file_path_here#")
print(f"The average score is: {avg}")