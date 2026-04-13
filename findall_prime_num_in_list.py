"""
Python Task-4
2.) Given a Python List [10, 501, 22, 37, 100, 999, 87, 351],
    your task is to Count all the Prime Numbers and create a new
    Python List which will contain all the Prime Numbers in it ?
"""

# Given python list declared globally
org_list = [10, 501, 22, 37, 100, 999, 87, 351]

def main():
    prime_num_list = [] # Empty list initialized for adding prime nos
    num_factor_dict = {} # Empty dictionary initialized for adding (number, factors) as (key, values)pairs
    fact_list = []

    for num in org_list:

        # Loop to check for the factors of each number apart from 1
        for i in range(2, num+1):
            if num % i == 0:
                fact_list.append(i) # Factors added as list for each number
        num_factor_dict[num] = fact_list # For each key as number, the factor_list becomes value
        fact_list = [] # Clearing  factor list before checking for next number

    # If each num has factor = num itself, then prime
    for num, fact_list in num_factor_dict.items():
        if len(fact_list) == 1 and num in fact_list:
            prime_num_list.append(num)

    print("Original List: ", org_list)
    print("Count of prime numbers in given list: ", len(prime_num_list))
    print("List containing all PRIME numbers from given List: ", prime_num_list)

if __name__ == "__main__":
    main()