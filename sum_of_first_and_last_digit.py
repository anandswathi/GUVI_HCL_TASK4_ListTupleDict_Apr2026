"""
4.) Write a python program to find the sum of the first and last digit of an integer ?
"""

def find_sum_of_first_and_last_digits(num):
    """
    Function to find the sum of first and last digit of an integer
    Input: num(Integer) as input
    Return: Sum of first and last digit of an integer
    """

    # List to store the digits in a num
    digit_list = []

    # Find digits and add to digit list
    while num > 0:
        digit = num % 10
        digit_list.append(digit)
        num = num // 10
    # Re-arrange digits in order
    digit_list = digit_list[::-1]

    return sum([digit_list[0], digit_list[-1]])

def main():

    # Get number as input from user
    num = int(input("\nEnter a number with at least 2 digits: "))

    sum_of_first_and_last_digits = find_sum_of_first_and_last_digits(num)
    print("Sum of first and last digit of an integer {}: {}".format(num, sum_of_first_and_last_digits))

if __name__ == "__main__":
    main()