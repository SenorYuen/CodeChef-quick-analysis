import json

# Path to the input JSON file
input_file = "final_successful_dataset.json"
output_file = "collected_codes.py"  # Changed to .py file for Python format

# Read the JSON data
with open(input_file, 'r') as file:
    data = json.load(file)

# Initialize a list to collect all code snippets
collected_codes = []

# Iterate through the JSON structure to extract code snippets
for problem_id, problem_details in data.items():
    # Check if 'human_solutions' is directly in problem_details or nested deeper
    if isinstance(problem_details, dict) and "human_solutions" in problem_details:
        for solution in problem_details["human_solutions"]:
            if "code" in solution:
                collected_codes.append(solution["code"])
    else:
        # If 'human_solutions' is not directly in problem_details, check deeper
        for key, sub_details in problem_details.items():
            if isinstance(sub_details, dict) and "human_solutions" in sub_details:
                for solution in sub_details["human_solutions"]:
                    if "code" in solution:
                        collected_codes.append(solution["code"])

# Write the collected code snippets to a Python file with separators
with open(output_file, 'w') as file:
    for code in collected_codes:
        file.write(code + "\n\n")  # Write the code snippet
        file.write("#--------------------------\n\n")  # Insert the comment separator

print(f"Collected {len(collected_codes)} code snippets.")
print(f"Output written to {output_file}")
