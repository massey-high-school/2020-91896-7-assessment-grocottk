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

        for yes_no_item in to_check:

            # If the response is in the list, return the response

            if response == yes_no_item:

                return response

            # if the response is one letter and is either a 'y' or 'n', return the corresponding answer.

            elif response == yes_no_item[0]:

                return yes_no_item

        # Otherwise, print an error message

        print("Please enter either Yes or a No")
