# Non - UI functions

# These functions are for the first type of sequence
def check_equality(number1, number2):
    """
    Check if two complex numbers are equal
    :param number1: The first number
    :param number2: The second number
    :return: 1 if the numbers are equal, 0 otherwise
    """
    if get_real_part(number1) == get_real_part(number2) and get_imaginary_part(number1) == get_imaginary_part(number2):
        return 1
    else:
        return 0


def distinct_sequence(complex_numbers):
    """
    Find the longest sequence of distinct complex numbers.
    :param complex_numbers: The list of complex numbers
    :return: A list consisting of the longest sequence of distinct complex numbers
    """
    max_length = 0
    answer = []

    for i in range(0, len(complex_numbers)):
        for j in range(i, len(complex_numbers)):
            # We check every sequence from i to j
            ok = 1  # We assume the sequence is correct
            for k in range(i, j+1):
                # For every element in the sequence (i;j)
                # we check if there is another complex number equal with it
                for q in range(k+1, j+1):
                    if check_equality(complex_numbers[k], complex_numbers[q]):
                        ok = 0
                        break

                if ok == 0:
                    break  # There is no point going further

            if ok == 1:  # If it's still 1, it means the sequence has only distinct numbers
                length = j - i + 1
                # This means we found a bigger sequence than what we already have and we update the new sequence
                if length > max_length:
                    max_length = length
                    answer = complex_numbers[i:j+1]

    return answer


# These functions are for the second type of sequence

def sum_real_part(complex_numbers, index1, index2):
    """
    Find the sum of the real parts of the numbers from a sequence (index1 -> index2)
    :param complex_numbers: The list of complex numbers
    :param index1: The starting position of the sequence
    :param index2: The end position of the sequence
    :return: The actual sum
    """
    s = 0
    for i in range(index1, index2 + 1):
        s += get_real_part(complex_numbers[i])

    return s


def sum_imaginary_part(complex_numbers, index1, index2):
    """
    Find the sum of the imaginary parts of the numbers from a sequence (index1 -> index2)
    :param complex_numbers: The list of complex numbers
    :param index1: The starting position of the sequence
    :param index2: The end position of the sequence
    :return: The actual sum
    """
    s = 0
    for i in range(index1, index2 + 1):
        s += get_imaginary_part(complex_numbers[i])

    return s


def sum_sequence(complex_numbers):
    """
    Find the longest sequence of complex numbers with the sum = 10 + 10i
    :param complex_numbers: The list of complex numbers
    :return: A list consisting of the longest sequence of complex numbers with the sum = 10 + 10i
    """
    max_length = 0
    answer = []
    for i in range(0, len(complex_numbers)):
        for j in range(i, len(complex_numbers)):
            # We check every sequence from i to j
            if sum_real_part(complex_numbers, i, j) == 10 and sum_imaginary_part(complex_numbers, i, j) == 10:
                length = j - i + 1
                # This means we found a bigger sequence than what we already have and we update the new sequence
                if length > max_length:
                    max_length = length
                    answer = complex_numbers[i:j + 1]

    return answer


# These functions are related to the complex numbers
def create_complex_number(real_part, imaginary_part):
    return real_part, imaginary_part


def add_complex_number(complex_numbers, real_part, imaginary_part):
    z = create_complex_number(real_part, imaginary_part)
    complex_numbers.append(z)


def get_real_part(number):
    return number[0]


def get_imaginary_part(number):
    return number[1]


def init_list():
    return [(1, 1), (2, 2), (2, 2), (5, 6), (10, 10), (0, 0), (0, 1), (1, 0),
            (2, 2), (2, 2), (2, 2), (4, 4), (0, 0)]


def print_numbers(complex_numbers):
    answer = "Your sequence is: "
    for number in complex_numbers:
        answer += str(get_real_part(number))

        if get_imaginary_part(number) != 0 and get_imaginary_part(number) != 1 and get_imaginary_part(number) != -1:
            if get_imaginary_part(number) > 0:
                answer += "+" + str(get_imaginary_part(number)) + "i, "
            else:
                answer += str(get_imaginary_part(number)) + "i, "
        elif get_imaginary_part(number) == 1:
            answer += "+i, "
        elif get_imaginary_part(number) == -1:
            answer += "-i, "
        else:
            answer += ', '

    answer = answer[:-2]  # Remove the last comma and space from the end
    return answer


# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_menu():
    print("\tHi there! What do you want to do?")
    print("\tPress 1 - I want to add a complex number to the list.")
    print("\tPress 2 - I want to display the list containing all the complex numbers.")
    print("\tPress 3 - Display the longest sequence of numbers containing only distinct numbers.")
    print("\tPress 4 - Display the longest sequence of numbers with the sum equal with 10+10i.")
    print("\tPress 5 - Exit the application.")


def input_real_part():
    try:
        real_part = int(input("Write the real part of the complex number: "))
        return real_part
    except ValueError:
        return None


def input_imaginary_part():
    try:
        imaginary_part = int(input("Write the imaginary part of the complex number: "))
        return imaginary_part
    except ValueError:
        return None


def read_complex_number(complex_numbers):
    real_part = input_real_part()
    imaginary_part = input_imaginary_part()

    if imaginary_part is None or real_part is None:
        print("Invalid input")
    else:
        add_complex_number(complex_numbers, real_part, imaginary_part)


def start():
    complex_numbers = init_list()

    while True:
        print_menu()
        option = (input())
        if option == '1':
            read_complex_number(complex_numbers)
        elif option == '2':
            print(print_numbers(complex_numbers))
        elif option == '3':
            print(print_numbers(distinct_sequence(complex_numbers)))
        elif option == '4':
            print(print_numbers(sum_sequence(complex_numbers)))
        elif option == '5':
            return
        else:
            print("Invalid input!!")


start()
