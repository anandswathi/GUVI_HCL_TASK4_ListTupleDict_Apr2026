"""
Python task-4
10.) Given a list [4, 2, -3, 1, 6]
    Write a python program to find if there is a sub-list with sum equal to Zero ?
"""
# Define given list globally
given_list = [4, 2, -3, 1, 6]

def check_sublist_with_zero(num_list):
    """
    Function to check if a list contains sub-list with sum equal to Zero
    Input: Takes input as the num_list
    Output: Prints sub-list with sum equal to Zero if it exists
    """
    num_list = given_list # List to check for the sub-list
    check_status = False # Status variable initialized
    l = len(num_list)

    # Check all possible sublists
    for i in range(l):
        curr_sum = 0
        for j in range(i, l):
            curr_sum += num_list[j]

            if curr_sum == 0:
                print("Sub-list with sum equal to Zero found. \nSub-list: ", num_list[i:j+1])
                check_status = True

    if not check_status:
        print("No sub-list with sum equal to zero found")

def main():
    print("Given python list: ", given_list)
    check_sublist_with_zero(given_list)

if __name__ == "__main__":
    main()


