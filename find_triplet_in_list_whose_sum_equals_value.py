"""
Python Task-4
9.) You have been given a Python list [10, 20, 30, 9] and a value of 59.
    Write a python program to find the triplet in the list whose sum is equal to the given value ?
"""

# Define given list and given value globally
given_list = [10, 20, 30, 9]
given_value = 59

def main():

    # Nested for loop to check all possible triplets
    for i in range(len(given_list)):
        for j in range(i+1, len(given_list)):
            for k in range(j+1, len(given_list)):
                total_sum = given_list[i] + given_list[j] + given_list[k]
                if total_sum == 59:
                    triplet_in_list_whose_sum_equals_value = [given_list[i], given_list[j], given_list[k]]

    print("Given Python List: ", given_list)
    print("Given Value: ", given_value)
    print("Triplet in the given list whose sum is equal to the given value: ", triplet_in_list_whose_sum_equals_value)

if __name__ == "__main__":
    main()