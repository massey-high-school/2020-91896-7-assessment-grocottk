
# Geometry Assessment Post Usability Testing Outcome
# This program is a version of the Geometry Calculator which implements the changes and additions that have been
# ... suggested and observed during the Usability Testing associated with this program.
# ... This code essentially continues to build on the base of the Assembled Outcome by adding and altering
# ... progress that has already been made in that program.

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

In this program, you will first be expected to enter, from a selection of options, the name of the shape type 
that you would like to calculate the measurements of.

After this, you will be asked to enter the required measurements that will be used to calculate 
both the area and perimeter of your shape.

Finally, both the perimeter and area of your given shape will be printed, followed by a question
asking you whether you would like to calculate the answer to another question.

If you continue from the previous question, you will be able to repeat the above process.
If you instead, however, choose to end the program, a summary of the questions that you have calculated will be given, 
with all of the numbers in the summary being rounded to two decimal places.

In order to begin, please enter below the name of your desired shape.
    ''')

# Yes or No Checker (Checks whether an input is either Yes or a No)
# ... [Adapted from '02_yes_no_checker.py' by Ms. Gottschalk]
# ['chosen_list' implementation inspired by Ms. Gottschalk's 'string_checker'
# ... file in repl.it]


def yes_no(question, chosen_list):

    # Begin Loop

    valid = False
    while not valid:

        # Defines response variable

        response = input(question).lower()

        # Checks input against the Yes and No in the 'to_check' list

        for yes_no_item in chosen_list:

            # If the response is in the list, return the response

            if response == yes_no_item:

                return response

            # if the response is one letter and is either a 'y' or 'n', return the corresponding answer.

            elif response == yes_no_item[0]:

                return yes_no_item

        # Otherwise, print an error message

        print("Please enter either Yes or a No")

# Shape List Formatter (Formats 'valid_shapes' list in order to improve usability)
# Code adapted from '00_sandpit.py' created by Ms. Gottschalk.
# ... This code has been adapted through variable name changes and comments that describe the code's purpose


def shape_list_formatting():

    # Defines 'shape_list' variable

    shape_list = ""

    # Adds every item in the 'valid_shapes' list into a sentence

    for formatted_item in valid_shapes:

        # Adds spaces between each list item

        shape_list += ", "

        # Adds all items into the shape_list variable

        shape_list += formatted_item

    return shape_list

# Shape Checker (Checks to see which shape the user has chosen from the options given)
# ... [This program is a customised version of the '02_yes_no_checker.py' by Ms. Gottschalk which checks shape types]
# ['chosen_list' implementation inspired by Ms. Gottschalk's 'string_checker'
# ... file in repl.it]


def shape_choice(question, chosen_list):

    # Begin Loop

    valid = False
    while not valid:

        # Defines response variable (as well as converting input into all lowercase letters)

        response = input(question).lower()

        # Checks input against the valid shapes in the 'valid_shapes' list

        for shape_item in chosen_list:

            # If the response is in the valid shapes list, return the response

            if response == shape_item:

                return response

            # If a single letter us entered and matches the first letter of any of the shape names,
            # ... return the shape name.

            elif response == shape_item[0]:

                return shape_item

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

# List Appending Function (Appends chosen list with a variety of important statistics from round)
# (Personal refresh on how to use the 'append.' function taken from '10_assembled_outcome.py'
# ... by myself [Kahlil Grocott]) ['chosen_list' implementation inspired by Ms. Gottschalk's 'string_checker'
# ... file in repl.it]


def list_appending(chosen_list):

    # Appends the number of questions solved in the program up until this point to the chosen list

    chosen_list.append(questions_solved)

    # Appends the type of shape calculated in the round to the chosen list

    chosen_list.append(shape_type)

    # Appends the user's first given measurement of the shape to the chosen list

    chosen_list.append(first_metric)

    # Appends the user's second given measurement of the shape to the chosen list

    chosen_list.append(second_metric)

    # Appends the perimeter of the shape to the chosen list

    chosen_list.append(perimeter)

    # Appends the area of the shape to the chosen list

    chosen_list.append(area)

# *** Main Routine: ***

# * Defining Variables and Lists: *
# ... [Inspired by subheadings from '11_post_usability_testing_outcome.py' by Kahlil Grocott]

# Defines 'yes_no' list used by the Yes or No Checker

yes_no_list = ["yes", "no"]

# Defines the constant of 'PI', in order to simplify the circle equations later in the program.


PI = 3.14159265359

# Defines 'all_round_statistics' list that will ultimately contain all of the working
# ... and results from all Rounds of the program.


all_round_statistics = []

# Defines 'questions_solved' variable
# ... (Round Counting in program inspired by the GIST 'RPS_07.1_Round_Counter_Alone.py' by myself [Kahlil Grocott])

questions_solved = 0

# Defines list of valid shapes to check against

valid_shapes = ["square", "circle", "rectangle", "triangle"]

# * Calculator Introduction: *

# Prints Title

statement_generator("Welcome to the Geometry Calculator", "*")

# Asks User whether they have used the program before [Adapted from '02_yes_no_checker.py' by Ms. Gottschalk]

program_experience = yes_no("Have you used this program before? ", yes_no_list)

# If the user answers yes, print an empty print statement and continue the program

if program_experience == "yes":

    print()

# Otherwise, if the user answers no, print the program's instructions, then continue the program

elif program_experience == "no":

    instructions()

# * Beginning of Round Loop: * (Code inspired by looping system in 'RPS_06_Loop_Game.py' by [Myself] Kahlil Grocott)

# Defines Loop Variable

loop = ""

# While the loop variable is defined as blank (or <enter>), continue the Round Loop

while loop == "":

    # Defines or 'Empties' the 'round_statistics' list at the beginning of every question asked

    round_statistics = []

    # Adds one to the program's 'questions_solved' variable in order to show as question information in final summary.
    # (Increment code inspired by https://reeborg.ca/docs/en/variables/increment.html)

    questions_solved += 1

    # * Receiving Shape Type: *

    # Prints the formatted and easily editable shape list to gain input from the user on their desired shape type

    shape_type = shape_choice("Please enter a shape from the following{} ".format(shape_list_formatting()),
                              valid_shapes)

    # If the desired shape is a square, carry out the following:

    if shape_type == valid_shapes[0]:

        # Basic question asking user for shape measurement input.

        first_metric = number_checker("Please enter the the value, without unit names, of the length of one of the "
                                      "sides of your square in centimeters ")

        # Defines the 'second_metric' variable as '0', in order to allow for result formatting.

        second_metric = 0

        # Runs User input through equation related to shape type

        perimeter = float(first_metric) * 4

        area = float(first_metric) * float(first_metric)

        # Prints the perimeter and area taken from user's input

        print('''
The perimeter of your square is {:.2f}cm,
while the area of your square is {:.2f}cm squared'''.format(perimeter, area))

        # Calls List Appending Function in order to append all important statistics to 'round_statistics' list

        list_appending(round_statistics)

    # Otherwise, if the desired shape is a circle, carry out the following:

    elif shape_type == valid_shapes[1]:

        # Basic question asking user for shape measurement input.

        first_metric = number_checker("Please enter the value, without unit names, of the radius "
                                      "of your circle in centimeters ")

        # Defines the 'second_metric' variable as '0', in order to allow for result formatting.

        second_metric = 0

        # Runs User input through equation related to shape type

        # Equations inspired by information from the website "Math Planet", at the following link:
        # 'https://www.mathplanet.com/education/pre-algebra/
        # more-about-equation-and-inequalities/calculating-the-circumference-of-a-circle'

        # A Circle calculation widget from 'Wolfram Alpha' was also used in the development of this program at the
        # ... following link: https://www.wolframalpha.com/widgets/gallery/view.jsp?id=e0d0f4c329f9c25d945e3b500541150a

        perimeter = 2 * PI * float(first_metric)

        area = PI * (float(first_metric) * float(first_metric))

        # Prints the perimeter and area taken from user's input

        print('''
The circumference of your provided circle is {:.2f}cm,
while the area of your circle is {:.2f}cm squared'''.format(perimeter, area))

        # Calls List Appending Function in order to append all important statistics to 'round_statistics' list

        list_appending(round_statistics)

    # Otherwise, if the desired shape is a rectangle, carry out the following:

    elif shape_type == valid_shapes[2]:

        # Basic question asking user for shape measurement input.

        first_metric = number_checker("Please enter the value, without unit names, of the length of the shortest side "
                                      "of your rectangle in centimeters ")

        # Basic question asking user for the second required shape measurement.

        second_metric = number_checker("Please enter the value, without unit names, of the length of the longest side "
                                       "of your rectangle in centimeters ")

        # Runs User input through equation related to shape type

        perimeter = (float(first_metric) * 2) + (float(second_metric) * 2)

        area = float(first_metric) * float(second_metric)

        # Prints the perimeter and area taken from user's input

        print('''
The perimeter of your rectangle is {:.2f}cm,
while the area of your rectangle is {:.2f}cm squared'''.format(perimeter, area))

        # Calls List Appending Function in order to append all important statistics to 'round_statistics' list

        list_appending(round_statistics)

    # Otherwise, if the desired shape is a triangle, carry out the following:

    elif shape_type == valid_shapes[3]:

        # Basic question asking user for shape measurement input.

        first_metric = number_checker("Please enter the value, without unit names, of the length of the base "
                                      "of your triangle in centimeters ")

        # Basic question asking user for the second required shape measurement.

        second_metric = number_checker("Please enter the value, without unit names, of the total vertical height "
                                       "of your triangle in centimeters ")

        # Runs User input through equation related to shape type

        perimeter = float(first_metric) * 3

        area = (float(first_metric) * float(second_metric)) / 2

        # Prints the perimeter and area taken from user's input

        print('''
The perimeter of your triangle is {:.2f}cm,
while the area of your triangle is {:.2f}cm squared'''.format(perimeter, area))

        # Calls List Appending Function in order to append all important statistics to 'round_statistics' list

        list_appending(round_statistics)

    # Appends all individual round information into 'all_round_statistics' list

    all_round_statistics.append(round_statistics)

    # Asks the user whether they would like to exit the Round Loop

    loop = input('''
Would you like to calculate the measurements of another shape?
Enter <enter> to continue, or any other key to exit the Geometry Calculator ''')
    print()

# * Calculator Conclusion: *

# Formatted Information array (original inspiration taken from many sources, including 'geekidharsh' on
# ... stackoverflow.com, however inspiration ultimately taken from Ms. Gottschalk's 'sandpit.py' file, the contents of
# ... which will be pasted below:)

# big_list = [[1, 'triangle', 5.0, 6.0, 15.0], [1, 'rectangle', 5.0, 6.0, 22.0, 30.0],
# [1, 'rectangle', 4.0, 3.0, 14.0, 12.0]]

# for item in big_list:
#     print("{} area {} perimeter {}".format(item[1], item[3], item[4]))

for item in all_round_statistics:

    print('''
Question {}:

    Shape Type: {}
    First User Input: {:.2f}
    Second User Input (if applicable): {:.2f}
    Perimeter of Shape: {:.2f}
    Area of Shape: {:.2f}'''.format(item[0], item[1], item[2], item[3], item[4], item[5]))

# Thanks the user for using the Geometry Calculator before exiting the program.

statement_generator("Thank you for using the Geometry Calculator", "@")
