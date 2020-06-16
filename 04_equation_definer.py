
# Geometry Assessment Component 4
# This Component defines 4 separate functions that each contain an equation for a given shape type.

# *** Functions: ***

# Instructions Function (Prints the instructions to the program for first time users,
# while also advising against cheating.) [Formatting Credit to 'The Python Cheat Sheet' and 'Noobmaster69']


def instructions():

    print('''
Welcome to the Geometry Calculator,

This program is intended for use by Intermediate School Students to assist in the completion of geometric equations.

In this program, you will be expected to enter the name of the shape type that you would like to calculate,
followed by the desired results and the required lengths that must be used.

After this, the answer to your specific result (either perimeter or area) will be given,
with the program asking whether if you would like to solve more shape problems.

Finally, after all shapes have been entered,
a summary of the working done by the program will be printed to end the program.

[Disclaimer: This program is intended for use as an educational tool.
The use of this program for any other function is strongly discouraged.]

Please begin the program by entering the name of your desired shape.
    ''')

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

# *** Main Routine: ***

# * Receiving Shape Type: * [Inspired by subheadings from '11_post_usability_testing_outcome.py' by Kahlil Grocott]

# Prints the formatted, editable shape list to gain input

shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()))

# Prints the user's shape choice for testing

print('''
You chose the {}
'''.format(shape_type))

# * Printing Shape Equation(s): *
