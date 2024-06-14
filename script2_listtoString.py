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


my_listcha1 = ['36', '36', '64', '36', '36', '37', '36', '66', '64', '68', '70', '69', '68', '64', '58', '36', '38', '39', '40', '41', '42', '43', '53', '44', '45', '71', '57', '72', '73', '73', '74', '75', '76', '77', '78', '79', '64', '7', '61', '62', '63', '63', '80', '67', '65', '65', '31', '32', '32', '34', '35', '46', '47']

my_listcha2 = ['50', '51', '52', '54', '51', '28', '52', '54', '52', '54', '52', '52', '52', '56', '52', '54', '48', '49', '21', '52', '16', '16', '55', '21', '14', '26', '25', '30', '21', '21', '21', '26', '21', '26', '54', '21', '26', '54', '54', '26', '16', '54', '26', '26', '23', '22', '12', '21', '22', '23', '11', '22', '24']

my_listcha3 = ['2', '27', '28', '29', '17', '26', '30', '12', '1', '24', '26', '15', '17', '21', '13', '17', '60', '22', '23', '16', '91', '4', '5', '4', '6', '8', '4', '5', '1', '4', '5', '6', '4', '6', '1', '1', '18', '21', '14', '20', '1', '4', '3', '5', '3', '1', '5', '1', '3', '3', '5', '5', '6', '6', '10', '10', '1', '4', '6', '92', '6', '9', '9', '8', '33', '10', '10', '18', '20', '19', '2', '5', '2', '5']

my_listcha4 = ['93', '89', '89', '90', '90']


integer_list = []
for item in my_listcha4:
  try:
      # Attempt conversion to integer
      integer_list.append(int(item))
  except ValueError:
      # Handle non-numeric values gracefully
      print(f"WARNING: Could not convert '{item}' to an integer.")

integer_list.sort()
string_representation = list_to_string(integer_list)
print(string_representation)
