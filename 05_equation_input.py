
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
triangle_side = 0
triangle_height = 0

# Defines list of equations associated with various shape types

text_equation_types = [["length * 4", "length * length"], ["(radius * 2) * π", "π * (radius^2)"],
                       ["(base * 2) + (height * 2)", "base * height"], ["side * 3", "side * triangle_height"]]

# Defines list of equations associated with various shape types, without quotation marks.
# ... (These should be used in the final program)

equation_types = [[length * 4, length * length], [(radius * 2) * PI, PI * (radius ^ 2)],
                  [(base * 2) + (height * 2), base * height], [triangle_side * 3, triangle_side * triangle_height]]

# *** Main Routine: ***

# * Receiving Shape Type: * [Inspired by subheadings from '11_post_usability_testing_outcome.py' by Kahlil Grocott]

# Prints the formatted, editable shape list to gain input

shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()))

# Prints the user's shape choice for testing

print('''
You chose the {}'''.format(shape_type))

# Uses 'if' and 'elif' statements in order to link input and corresponding equation
# (This code is currently inefficient and will most likely need to be improved.)
# [This function has been adapted from its use in Component 4, where in this program,
# ... its functionality as a piece of code will be improved.)

equation_choice = ""

if shape_type == valid_shapes[0]:

    text_equation = (text_equation_types[0])

elif shape_type == valid_shapes[1]:

    text_equation = (text_equation_types[1])

elif shape_type == valid_shapes[2]:

    text_equation = (text_equation_types[2])

elif shape_type == valid_shapes[3]:

    text_equation = (text_equation_types[3])

print('''
The equations associated with {}s are:

'{}' and

'{}'
'''.format(shape_type, text_equation[0], text_equation[1]))
