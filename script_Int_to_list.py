def get_integers_and_print_as_list():
  """Prompts the user for integers and prints them as a list enclosed in square brackets.

  Handles potential errors if the user enters non-numeric input.
  """
  numbers = []
  while True:
    try:
      # Get user input as a string
      number_str = input("Enter an integer (or 'q' to quit): ")
      if number_str.lower() == 'q':
        break

      # Convert the input to an integer
      number = int(number_str)
      numbers.append(number)
    except ValueError:
      print("Invalid input. Please enter an integer.")

  # Print the list of integers enclosed in square brackets
  if numbers:
    numbers.sort()
    print(numbers)
  else:
    print("No integers were entered.")



get_integers_and_print_as_list()

