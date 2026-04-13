"""
8.) Write a python program to find the minimum element in a rated and sorted list ?
"""

def main():
    # Define a list for given list
    sorted_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print("Given sorted list : ",sorted_list)

    # Rotated sorted list
    rotated_sorted_list = [10,11,12,13,14,15,1,2,3,4,5,6,7,8,9]
    print("Rotated list : ",rotated_sorted_list)

    # Initializing min element as first element in list
    min_element = rotated_sorted_list[0]

    # Logic to find the min element in list
    for element in rotated_sorted_list:
        if element < min_element:
            min_element = element

    print("Minimum element in a rotated and sorted list : ",min_element)

if __name__ == "__main__":
    main()

