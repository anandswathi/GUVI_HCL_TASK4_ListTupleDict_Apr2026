"""
5.) How can I use Python to find all the ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5, and Rs. 10 coins ?
"""

def main():

    # Define Counter variable for counting the no. of ways
    # to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5, and Rs. 10 coins
    no_of_ways = 0

    # Checking all possible combinations
    for rupee_1 in range(11):
        for rupee_2 in range(6):
            for rupee_5 in range(3):
                for rupee_10 in range(1):
                    total = rupee_1*1 + rupee_2*2 + rupee_5*5 + rupee_10*10
                    if total == 10:
                        print("1 Rupee: {}, 2 Rupee: {}, 5 Rupee: {}, 10 Rupee: {}".format(rupee_1, rupee_2, rupee_5, rupee_10))
                        no_of_ways += 1

    print("Total number of ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5, and Rs. 10 coins: {}".format(no_of_ways))

if __name__ == "__main__":
    main()