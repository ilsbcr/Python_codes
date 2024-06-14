def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    unique_list = list(set(input_list))
    # Sort the list to maintain order (if needed)
    unique_list.sort(key=int)
    return unique_list

def format_output(unique_list):
    # Format the list as per the required output
    formatted_list = ' '.join(f'[{item}]' for item in unique_list)
    return formatted_list

# Example usage
input_str = input("Enter a list of numbers enclosed in square brackets, separated by spaces: ")
# Parse the input string
input_list = input_str.replace('[', '').replace(']', '').split()
# Remove duplicates
unique_list = remove_duplicates(input_list)
# Format the output
result = format_output(unique_list)
# Print the result
print(f"the result : {result}")
