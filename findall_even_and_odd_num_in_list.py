"""
Python Task-4
1.) You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351]
    your task is to create two List one which have all the Even Numbers and
    another List which will have all the ODD numbers in it ?
"""

# Given python list declared globally
org_list = [10, 501, 22, 37, 100, 999, 87, 351]

def main():
    """
    1.) You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two List one which have all the Even Numbers and another List which will have all the ODD numbers in it ?
    """
    even_num_list = [] # Empty List initialized for adding even numbers
    odd_num_list = [] # Empty List initialized for adding odd numbers

    for element in org_list:
        # If condition to check for even no
        if element % 2 == 0:
            even_num_list.append(element)

        # If condition fails then odd no
        else:
            odd_num_list.append(element)

    print("Original List: ", org_list)
    print("List containing all EVEN numbers from Original List: ", even_num_list)
    print("List containing all ODD numbers from Original List: ", odd_num_list)


if __name__ == "__main__":
    main()


