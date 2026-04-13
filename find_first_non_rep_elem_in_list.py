"""
7.) Write a python program to find the first non–repeating elements in a given list of integers ?
"""

def main():
    # Given list of integers
    given_list = [1,2,3,44,5,90,781,888,1,2,30,234,72,59,46,4,0,1000,56,0,0,0,0,5,6,4]

    # Calculate the frequency of each element in list
    for element in given_list:
        if given_list.count(element) == 1: #Checking if the integer is non-repeating
            print("First non-repeating element in the given list : ",element)
            break
    else:
        print("No non-repeating element found in the given list")

if __name__ == "__main__":
    main()