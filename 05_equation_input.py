
# Geometry Assessment Component 5
# This Component asks the user for the type of their shape, and a specific measurement associated with that shape.

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

# Equation Definer (Defines all equations applicable with program for both Perimeter and Area.)
# [This code has now been entered into the Main Routine of the Component]

# Defines undefined variables (and constant) [for testing] (pairs with equation list without quotation marks)

length = 0
radius = 0
PI = 3.14159265359
base = 0
height = 0
triangle_base = 0
triangle_height = 0
first_unit = 0
second_unit = 0

# Defines list of equations associated with various shape types

text_equation_types = [["length * 4", "length * length"], ["(radius * 2) * π", "π * (radius^2)"],
                       ["(base * 2) + (height * 2)", "base * height"], ["side * 3", "side * triangle_height"]]

# Defines list of equations associated with various shape types, without quotation marks.
# ... (These should be used in the final program)

equation_types = [[float(first_unit) * 4, float(first_unit) * float(first_unit)],
                  [(float(first_unit) * 2) * PI, PI * (float(first_unit) * float(first_unit))],
                  [(float(first_unit) * 2) + (float(second_unit) * 2), float(first_unit) * float(second_unit)],
                  [float(first_unit) * 3, float(first_unit) * float(second_unit)]]

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

            print(error)

# *** Main Routine: ***

# * Receiving Shape Type: * [Inspired by subheadings from '11_post_usability_testing_outcome.py' by Kahlil Grocott]

# Prints the formatted, editable shape list to gain input

shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()))

# Prints the user's shape choice for testing

print('''
You chose the {}'''.format(shape_type))

# * Printing Shape Equation(s): *

# Uses 'if' and 'elif' statements in order to link input and corresponding equation
# (This code is currently inefficient and will most likely need to be improved.)
# [This function has been adapted from its use in Component 4, where in this program,
# ... its functionality as a piece of code will be improved.)

equation_choice = ""

if shape_type == valid_shapes[0]:

    text_equation = text_equation_types[0]
    first_unit_name = "length"
    second_unit_name = ""
    first_unit = length
    equation = equation_types[0]

# Idea for updated input method after trialing:

    # Prints Follow-Up question, if needed, based on shape type

    # Places given variable input into respective equation (without calling from list)

    # Gives user answer (may be able to be given outside of loop)

# This idea would then be repeated for all shape types in order to complete Component Requrements.


elif shape_type == valid_shapes[1]:

    text_equation = text_equation_types[1]
    first_unit_name = "radius"
    second_unit_name = ""
    first_unit = radius
    equation = equation_types[1]

elif shape_type == valid_shapes[2]:

    text_equation = text_equation_types[2]
    first_unit_name = "base"
    second_unit_name = "height"
    first_unit = base
    second_unit = height
    equation = equation_types[2]

elif shape_type == valid_shapes[3]:

    text_equation = text_equation_types[3]
    first_unit_name = "base"
    second_unit_name = "height"
    first_unit = triangle_base
    second_unit = triangle_height
    equation = equation_types[3]

# Prints the user with a text-based version of the equations provided in the program.

print('''
The equations associated with {}s are:

'{}' and

'{}'
'''.format(shape_type, text_equation[0], text_equation[1]))

# Basic question asking user for shape measurement input.

first_unit = number_checker("Please enter the {} of your {} in centimeters ".format(first_unit_name, shape_type))

# Prints user response to first question

print()
print("The {} of your {} is {:.2f}cm".format(first_unit_name, shape_type, first_unit))

# If there is a required second input in order to calculate a shape's measurements,
# ... print the provided second measurement (when applicable)

if second_unit_name != "":

    print()
    second_unit = number_checker(
        "Now, please enter the {} of your {} in centimeters ".format(second_unit_name, shape_type))

    # Prints user response to second question

    print()
    print("The {} of your {} is {:.2f}cm".format(second_unit_name, shape_type, second_unit))

else:

    print()
    print("Okay")

# Prints the solution to the relevant equation

print()
print(equation)
