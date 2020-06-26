
# Geometry Assessment Component 6
# This Component asks the user to specify the required measurements that they require to be outputted
# ... at the end of the round.

# *** Functions: ***

# Shape List Formatter (Formats 'valid_shapes' list in order to improve usability)
# [Code adapted from '00_sandpit.py' created by Ms. Gottschalk.
# ... This code has been adapted through variable name changes and comments that describe the code's purpose]


def shape_list_formatting():

    # Defines 'shape_list' variable

    shape_list = ""

    # Adds every item in the 'valid_shapes' list into a sentence

    for item in valid_shapes:

        # Adds spaces between each list item

        shape_list += ", "

        # Adds all items into the shape_list variable

        shape_list += item

    return shape_list

# Shape Checker (Checks to see which shape the user has chosen from the options given)
# ... [This program is a customised version of the '02_yes_no_checker.py' by Ms. Gottschalk which checks shape types]

# Defines list of valid shapes to check against

valid_shapes = ["square", "circle", "rectangle", "triangle"]


def shape_choice(question):

    # Begin Loop

    valid = False
    while not valid:

        # Defines response variable (as well as converting input into all lowercase letters)

        response = input(question).lower()

        # Checks input against the valid shapes in the 'valid_shapes' list

        for item in valid_shapes:

            # If the response is in the valid shapes list, return the response

            if response == item:

                return response

            # If a single letter us entered and matches the first letter of any of the shape names,
            # ... return the shape name.

            elif response == item[0]:

                return item

        # Otherwise, print an error message

        print("Please enter a valid shape from{}".format(shape_list_formatting()))

# Defines the constant of 'PI', in order to simplify the circle equations later in the program.

PI = 3.14159265359

# Number Checking Function (For floats [Numbers that allow the use of decimal points] greater than zero):
# ... [This code was taken from Kahlil Grocott's '11_post_usability_testing_outcome.py']


def number_checker(question):

    # Defines Error Message

    error = "Please enter a number (decimal places allowed) that is more than zero."

    # Beginning of Loop

    valid = False
    while not valid:

        try:

            response = float(input(question))

            # If response is less than or equal to zero, print the error message

            if response <= 0:

                print(error)

            # Otherwise, return the user's response

            else:

                return response

        # If a value error is present, print the error message

        except ValueError:

            print(error)\

# Specific Measurement Checker (Checks to see which measurement type has been chosen from the two options given)
# ... [This program is a customised version of the '02_yes_no_checker.py' by Ms. Gottschalk which checks shape types]
# ... (This program is also adapted from the above shape checker)

# Defines list of valid specific measurents to check against

measurement_types = ["area", "perimeter"]


def measurement_choice(question):

    # Begin Loop

    valid = False
    while not valid:

        # Defines response variable (as well as converting input into all lowercase letters)

        response = input(question).lower()

        # Checks input against the valid shapes in the 'measurement_types' list

        for item in measurement_types:

            # If the response is in the measurement types list, return the response

            if response == item:

                return response

            # If either of the letters 'a' or 'e' are entered, return the corresponding measurement type.

            elif response == item[0]:

                return item

        # Otherwise, print an error message

        print("Please enter either 'Perimeter' or 'Area' ")

# *** Main Routine: ***

# Asks the user for their desired measurement type, between the options of 'Perimeter' or 'Area'

area_or_perimeter = measurement_choice("What are the measurements that you would like to calculate "
                                       "for your chosen shape. Please enter either ‘Perimeter’ or ‘Area’ ")

# If the user chooses to find the area, print a given message

if area_or_perimeter == "area":

    print("You have chosen to find the area of your shape")
    print()

    # Prints the possible equations, and required measurements for those equations.

    print("The equation for the area of a square is length * length, meaning that length must be entered")
    print()
    print("The equation for the area of a circle is π * (radius^2), meaning that the radius must be entered")
    print()
    print("The equation for the area of a rectangle is base * height, "
          "meaning that both the base and height of the rectangle must be entered")
    print()
    print("The equation for the area of a triangle is triangle side * triangle height, "
          "meaning that both the base and height of your triangle must be entered")

# If the user chooses to find the perimeter, print a given message

elif area_or_perimeter == "perimeter":

    print("You have chosen to find the perimeter of your shape")
    print()

    # Prints the possible equations, and required measurements for those equations.

    print("The equation for the perimeter of a square is length * 4, meaning that length must be entered")
    print()
    print("The equation for the area of a perimeter is (radius * 2) * π, meaning that the radius must be entered")
    print()
    print("The equation for the perimeter of a rectangle is (base * 2) + (height * 2), "
          "meaning that both the base and height of the rectangle must be entered")
    print()
    print("The equation for the perimeter of a triangle is side * 3, "
          "meaning that only the length of the side of your triangle must be entered")
