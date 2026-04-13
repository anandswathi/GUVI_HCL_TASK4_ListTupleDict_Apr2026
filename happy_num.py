"""
3.) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351]
    Find out how many numbers are there in the given Python List which are Happy Numbers ?
"""

# Define given list globally
org_list = [10, 501, 22, 37, 100, 999, 87, 351]

def get_sum_of_squares_of_digits(num):
    """
    Func to find the sum of squares of digits in a number
    Input: num(Int) as input
    Return: Sum of squares of digits
    """
    # List to store the digits in a num
    sq_of_digit_list = []

    # Split digits, find square and add to digit list
    for el in str(num):
        sq_of_digit_list.append(int(el)**2)

    # Sum of squares of digits in num
    sum_of_squares_of_digits = sum(sq_of_digit_list)

    return sum_of_squares_of_digits

def check_happy_num(num):
    """
    Function to check if a given number is Happy Number or not
    Input: num(Int) as input
    Return: True if Happy Number else False
    """

    # For controlling while control
    looped_nums = set()

    # Check if sum of squares of digit in num is 1
    while num != 1 and num not in looped_nums:
        looped_nums.add(num)
        num = get_sum_of_squares_of_digits(num)

    # If sum is 1 then Happy num else Not Happy num
    if num == 1:
        return True
    else:
        return False

def main():
    # List to add the Happy nos. from given list
    happy_num_list = []

    # Add Happy num to happy_num_list
    for num in org_list:
        check_status = check_happy_num(num)
        if check_status:
            happy_num_list.append(num)

    print("The given Python List: {}".format(org_list))
    print("Total no. of happy numbers in the given Python List: {}".format(len(happy_num_list)))
    print("The {} Happy Numbers from the given Python List are:".format(len(happy_num_list)), end=" ")
    for num in happy_num_list:
        print(num, end=" ")

if __name__ == "__main__":
    main()


