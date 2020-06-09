
# Geometry Assessment Component 1
# This Component asks the user whether they have used the program before. If they have not,
# ... instructions will be printed, while if they have, instructions will not be printed.

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

# *** Main Routine: ***


# Prints Title

statement_generator("Welcome to the Geometry Calculator", "*")

# Asks User whether they have used the program before [Adapted from '02_yes_no_checker.py' by Ms. Gottschalk]

program_experience = yes_no("Have you used this program before? ")

# Prints Input for Testing

print('''
You said {}
'''.format(program_experience))

# If the user answers yes, (print) 'continue the program'

if program_experience == "yes":

    print("continue")

# If the user answers no, print the program's instructions

elif program_experience == "no":

    instructions()
    print("continue")
