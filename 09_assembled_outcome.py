
# Geometry Assessment Assembled Outcome
# The following program is the first version of the Geometry Calculator Program's Assembled Outcome.
# ... This program utilises previously created Components in order to create an outcome
# ... which aims to satisfy all of the program's requirements.

# *** Functions: ***

# Statement Generator (Finds the length of a message, and prints characters above and below that equal the
# ... length of the message) [Taken from MQA_Post_Usability_Testing_1.0 Gist created on October 29 2019]:


def statement_generator(message, character):
    print()
    print(len(message) * character)
    print(message)
    print(len(message) * character)
    print()

# Instructions Function (Prints the instructions to the program for first time users.)
# Formatting Credit to 'The Python Cheat Sheet' and 'Noobmaster69'


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

Please begin the program by entering the name of your desired shape.
    ''')

# Yes or No Checker (Checks whether an input is either Yes or a No)
# ... [Adapted from '02_yes_no_checker.py' by Ms. Gottschalk]


def yes_no(question):

    # Defines list to check against

    to_check = ["yes", "no"]

    # Begin Loop

    valid = False
    while not valid:

        # Defines response variable

        response = input(question).lower()

        # Checks input against the Yes and No in the 'to_check' list

        for item in to_check:

            # If the response is in the list, return the response

            if response == item:

                return response

            # if the response is one letter and is either a 'y' or 'n', return the corresponding answer.

            elif response == item[0]:

                return item

        # Otherwise, print an error message

        print("Please enter either Yes or a No")

# Shape List Formatter (Formats 'valid_shapes' list in order to improve usability)
# Code adapted from '00_sandpit.py' created by Ms. Gottschalk.
# ... This code has been adapted through variable name changes and comments that describe the code's purpose


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

# Defines the constant of 'PI', in order to simplify the circle equations later in the program.


PI = 3.14159265359

# Defines list of equations associated with various shape types


equation_types = [["length * 4", "length * length"], ["(radius * 2) * π", "π * (radius^2)"],
                  ["(base * 2) + (height * 2)", "base * height"], ["side * 3", "side * triangle_height"]]

# *** Main Routine: ***

# * Calculator initialisation: *


# Prints Title

statement_generator("Welcome to the Geometry Calculator", "*")

# Asks User whether they have used the program before [Adapted from '02_yes_no_checker.py' by Ms. Gottschalk]

program_experience = yes_no("Have you used this program before? ")

# If the user answers yes, continue the program

if program_experience == "yes":

    print()

# Otherwise, if the user answers no, print the program's instructions, then continue the program

elif program_experience == "no":

    instructions()

# *** Main Routine: ***

# Prints the formatted, editable shape list to gain input

shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()))

# Prints the user's shape choice for testing

print('''
You chose the {}
'''.format(shape_type))

# * Printing Shape Equation(s): *

# Uses 'if' and 'elif' statements in order to link input and corresponding equation
# (This code is currently inefficient and will most likely need to be improved.)

equation_choice = ""

if shape_type == valid_shapes[0]:

    equation_choice = (equation_types[0])

elif shape_type == valid_shapes[1]:

    equation_choice = (equation_types[1])

elif shape_type == valid_shapes[2]:

    equation_choice = (equation_types[2])

elif shape_type == valid_shapes[3]:

    equation_choice = (equation_types[3])

# Prints a text-based version of the equations provided in the program.

print('''
The equations associated with {}s are:

'{}' and

'{}'
'''.format(shape_type, equation_choice[0], equation_choice[1]))

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
