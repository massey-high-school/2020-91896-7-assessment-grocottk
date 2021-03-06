
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

# Defines the constant of 'PI', in order to simplify the circle equations later in the program.

PI = 3.14159265359

# Defines list of equations associated with various shape types

text_equation_types = [["length * 4", "length * length"], ["(radius * 2) * π", "π * (radius^2)"],
                       ["(base * 2) + (height * 2)", "base * height"], ["side * 3", "side * triangle_height"]]

# Defines list of equations associated with various shape types, without quotation marks.
# ... (These should be used in the final program)

# equation_types = [[float(first_unit) * 4, float(first_unit) * float(first_unit)],
#                   [(float(first_unit) * 2) * PI, PI * (float(first_unit) * float(first_unit))],
#                   [(float(first_unit) * 2) + (float(second_unit) * 2), float(first_unit) * float(second_unit)],
#                   [float(first_unit) * 3, float(first_unit) * float(second_unit)]]

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
You chose the {}
'''.format(shape_type))

# * Carrying out respective shape working: *

# Uses 'if' and 'elif' statements in order to link input and corresponding equation
# (This code is currently inefficient and will most likely need to be improved.)
# [This function has been adapted from its use in Component 4, where in this program,
# ... its functionality as a piece of code will be improved.]

# If the desired shape is a square, carry out the following:

if shape_type == valid_shapes[0]:

    # Basic question asking user for shape measurement input.

    length = number_checker("Please enter the length of one of the sides of your square in centimeters ")

    # Prints user response to first question

    print()
    print("The length of one side your square is {:.2f}cm".format(length))

    # Runs User input through equation related to shape type

    perimeter = float(length) * 4

    area = float(length) * float(length)

    # Prints the perimeter and area taken from user's input

    print('''
The perimeter of your square is {:.2f}cm,
while the area of your square is {:.2f}cm squared'''.format(perimeter, area))

# Otherwise, if the desired shape is a circle, carry out the following:

elif shape_type == valid_shapes[1]:

    # Basic question asking user for shape measurement input.

    radius = number_checker("Please enter the radius of your circle in centimeters ")

    # Prints user response to first question

    print()
    print("The radius of your circle is {:.2f}cm".format(radius))

    # Runs User input through equation related to shape type

    # Equations inspired by information from the website "Math Planet", at the following link:
    # 'https://www.mathplanet.com/education/pre-algebra/
    # more-about-equation-and-inequalities/calculating-the-circumference-of-a-circle'

    # A Circle calculation widget from 'Wolfram Alpha'
    # ... was also used in the development of this program at the following link:
    # https://www.wolframalpha.com/widgets/gallery/view.jsp?id=e0d0f4c329f9c25d945e3b500541150a

    perimeter = 2 * PI * float(radius)

    area = PI * (float(radius) * float(radius))

    # Prints the perimeter and area taken from user's input

    print('''
The circumference of your provided circle is {:.2f}cm,
while the area of your circle is {:.2f}cm squared'''.format(perimeter, area))

# Otherwise, if the desired shape is a rectangle, carry out the following:

elif shape_type == valid_shapes[2]:

    # Basic question asking user for shape measurement input.

    base = number_checker("Please enter the length of the shortest side of your rectangle in centimeters ")

    # Basic question asking user for the second required shape measurement.

    height = number_checker("Please enter the length of the longest side of your rectangle in centimeters ")

    # Prints user response to above question

    print()
    print("The base of your rectangle is {:.2f}cm, while the height of your rectangle is {:.2f}cm"
          .format(base, height))

    # Runs User input through equation related to shape type

    perimeter = (float(base) * 2) + (float(height) * 2)

    area = float(base) * float(height)

    # Prints the perimeter and area taken from user's input

    print('''
The perimeter of your rectangle is {:.2f}cm,
while the area of your rectangle is {:.2f}cm squared'''.format(perimeter, area))

# Otherwise, if the desired shape is a triangle, carry out the following:

elif shape_type == valid_shapes[3]:

    # Basic question asking user for shape measurement input.

    triangle_base = number_checker("Please enter the length of the base of your triangle in centimeters ")

    # Basic question asking user for the second required shape measurement.

    triangle_height = number_checker('''Please enter the height (from the base to the top of the equilateral triangle)
of your triangle in centimeters ''')

    # Prints user response to above question

    print()
    print("The base of your triangle is {:.2f}cm, while the height of your triangle is {:.2f}cm"
          .format(triangle_base, triangle_height))

    # Runs User input through equation related to shape type

    perimeter = float(triangle_base) * 3

    area = (float(triangle_base) * float(triangle_height)) / 2

    # Prints the perimeter and area taken from user's input

    print('''
The perimeter of your triangle is {:.2f}cm,
while the area of your triangle is {:.2f}cm squared'''.format(perimeter, area))
