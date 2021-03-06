
# Geometry Assessment Component 8
# This Component stores all of the user's previously entered input in a list,
# ... where the working and results are eventually printed and shown to the user.

# *** Functions: ***

# Statement Generator (Finds the length of a message, and prints characters above and below that equal the
# ... length of the message) [Taken from MQA_Post_Usability_Testing_1.0 Gist created on October 29 2019]:


def statement_generator(message, character):
    print()
    print(len(message) * character)
    print(message)
    print(len(message) * character)
    print()

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

            print(error)

# *** Main Routine: ***

# Defines 'all_round_statistics' list that will ultimately contain all of the working
# ... and results from all Rounds of the program.


all_round_statistics = []

# Beginning of Round Loop (Code inspired by looping system in 'RPS_06_Loop_Game.py' by [Myself] Kahlil Grocott)

# Defines 'questions_solved' variable
# ... (Round Counting in program inspired by the GIST 'RPS_07.1_Round_Counter_Alone.py' by myself [Kahlil Grocott])

questions_solved = 0

# Defines Loop Variable

loop = ""

# While the loop variable is defined as blank (or <enter>), continue the Round Loop

while loop == "":

    # Defines or 'Empties' the 'round_statistics' list at the beginning of every question

    round_statistics = []

    # Adds one to the program's 'questions_solved' variable in order to show Question information in final summary.

    questions_solved = questions_solved + 1

    # * Receiving Shape Type: * [Inspired by subheadings from '11_post_usability_testing_outcome.py' by Kahlil Grocott]

    # Prints the formatted, editable shape list to gain input

    shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()))

    # Prints the user's shape choice for testing

    print('''
You chose the {}
    '''.format(shape_type))

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

        # Appends list 'round_statistics' with all important statistics from Round
        # (Reminder of how to use the 'append.' function taken from '10_assembled_outcome.py'
        # ... by myself [Kahlil Grocott])

        # Appends the round's Round Number to the 'round_statistics' list

        round_statistics.append(questions_solved)

        # Appends the type of shape calculated in the round to the 'round_statistics' list

        round_statistics.append(valid_shapes[0])

        # Appends the user's given measurement of the shape to the 'round_statistics' list

        round_statistics.append(length)

        # Appends the perimeter of the shape to the 'round_statistics' list

        round_statistics.append(perimeter)

        # Appends the area of the shape to the 'round_statistics' list

        round_statistics.append(area)

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

        # Appends list 'round_statistics' with all important statistics from Round
        # (Reminder of how to use the 'append.' function taken from '10_assembled_outcome.py'
        # ... by myself [Kahlil Grocott])

        # Appends the round's Round Number to the 'round_statistics' list

        round_statistics.append(questions_solved)

        # Appends the type of shape calculated in the round to the 'round_statistics' list

        round_statistics.append(valid_shapes[1])

        # Appends the user's given measurement of the shape to the 'round_statistics' list

        round_statistics.append(radius)

        # Appends the perimeter of the shape to the 'round_statistics' list

        round_statistics.append(perimeter)

        # Appends the area of the shape to the 'round_statistics' list

        round_statistics.append(area)

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

        # Appends list 'round_statistics' with all important statistics from Round
        # (Reminder of how to use the 'append.' function taken from '10_assembled_outcome.py'
        # ... by myself [Kahlil Grocott])

        # Appends the round's Round Number to the 'round_statistics' list

        round_statistics.append(questions_solved)

        # Appends the type of shape calculated in the round to the 'round_statistics' list

        round_statistics.append(valid_shapes[2])

        # Appends the user's first given measurement of the shape to the 'round_statistics' list

        round_statistics.append(base)

        # Appends the user's second given measurement of the shape to the 'round_statistics' list

        round_statistics.append(height)

        # Appends the perimeter of the shape to the 'round_statistics' list

        round_statistics.append(perimeter)

        # Appends the area of the shape to the 'round_statistics' list

        round_statistics.append(area)

    # Otherwise, if the desired shape is a triangle, carry out the following:

    elif shape_type == valid_shapes[3]:

        # Basic question asking user for shape measurement input.

        triangle_base = number_checker("Please enter the length of the base of your triangle in centimeters ")

        # Basic question asking user for the second required shape measurement.

        triangle_height = number_checker('''Please enter the height
(from the base to the top of the equilateral triangle)
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

        # Appends list 'round_statistics' with all important statistics from Round
        # (Reminder of how to use the 'append.' function taken from '10_assembled_outcome.py'
        # ... by myself [Kahlil Grocott])

        # Appends the round's Round Number to the 'round_statistics' list

        round_statistics.append(questions_solved)

        # Appends the type of shape calculated in the round to the 'round_statistics' list

        round_statistics.append(valid_shapes[3])

        # Appends the user's first given measurement of the shape to the 'round_statistics' list

        round_statistics.append(triangle_base)

        # Appends the user's second given measurement of the shape to the 'round_statistics' list

        round_statistics.append(triangle_height)

        # Appends the perimeter of the shape to the 'round_statistics' list

        round_statistics.append(perimeter)

    # Appends all individual round information into 'all_round_statistics' list

    all_round_statistics.append(round_statistics)

    # Asks the user whether they would like to exit the Round Loop

    loop = input('''
Would you like to calculate the measurements of another shape?
Enter <enter> to continue, or any other key to exit the Geometry Calculator ''')
    print()

# Prints all information related to 'all_round_statistics' without formatting (for testing)

print(all_round_statistics)

# Thanks the user for using the Geometry Calculator before exiting the program.

statement_generator("Thank you for using the Geometry Calculator", "@")
