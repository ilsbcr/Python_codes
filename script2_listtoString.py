def list_to_string(input_list):
  """Converts a list to a string with each item enclosed in square brackets and separated by spaces.

  Args:
      input_list: The list to be converted.

  Returns:
      A string representation of the list with each item bracketed and separated by spaces.
  """
  formatted_string = ""
  for item in input_list:
    formatted_string += f"[{item}] "
  return formatted_string.rstrip()  # Remove trailing space

# Example usage
#my_list = [16, 17, 20, 21, 22, 24, 25, 26, 28, 30, 48, 49, 50, 51, 52, 53,  54, 55, 56, 57, 58]

my_list2 =['36', '36', '94', '36', '36', '37', '36', '36', '95', '96', '97', '98', '100', '99', '98', '36', '38', '36', '39', '40', '41', '42', '43', '122', '44', '45', '101', '123', '102', '103', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '114', '115', '116', '117', '117', '118', '119', '119', '120', '121', '46', '47']

my_list3 = ['2', '27', '28', '29', '17', '26', '30', '12', '1', '24', '26', '15', '17', '21', '13', '17', '35', '32', '31', '22', '23', '16', '4', '5', '4', '6', '8', '4', '5', '1', '4', '5', '6', '4', '6', '1', '1', '18', '21', '14', '20', '1', '4', '3', '5', '3', '1', '5', '1', '3', '3', '5', '5', '6', '6', '10', '10', '1', '4', '6', '6', '9', '9', '8', '33', '10', '10', '18', '20', '19', '2', '5', '2', '5']

my_listcha1 = ['36', '36', '94', '36', '36', '37', '36', '96', '97', '98', '100', '99', '98', '95', '124', '36', '38', '39', '40', '41', '42', '43', '122', '44', '45', '101', '123', '102', '103', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '114', '115', '116', '117', '117', '118', '119', '119', '120', '121', '46', '47']

my_listcha2 = ['50', '51', '52', '54', '51', '28', '52', '54', '52', '54', '52', '52', '52', '56', '52', '54', '48', '49', '21', '52', '16', '16', '55', '21', '14', '26', '25', '30', '21', '21', '21', '26', '21', '26', '54', '21', '26', '54', '54', '26', '16', '54', '26', '26', '23', '22', '12', '21', '22', '23', '11', '22', '24']

my_listcha3 = ['2', '27', '28', '29', '17', '26', '30', '12', '1', '24', '26', '15', '17', '21', '13', '17', '59', '60', '22', '23', '16', '4', '5', '4', '6', '8', '4', '5', '1', '4', '5', '6', '4', '6', '1', '1', '18', '21', '14', '20', '1', '4', '3', '5', '3', '1', '5', '1', '3', '3', '5', '5', '6', '6', '10', '10', '1', '4', '6', '6', '9', '9', '8', '33', '10', '10', '18', '20', '19', '2', '5', '2', '5']
integer_list = []
for item in my_listcha3:
  try:
      # Attempt conversion to integer
      integer_list.append(int(item))
  except ValueError:
      # Handle non-numeric values gracefully
      print(f"WARNING: Could not convert '{item}' to an integer.")

integer_list.sort()
string_representation = list_to_string(integer_list)
print(string_representation)
