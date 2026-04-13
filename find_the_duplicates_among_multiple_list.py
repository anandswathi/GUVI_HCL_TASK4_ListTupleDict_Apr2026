"""
6.) You have been given three lists. Your task is to find the duplicates in the three lists.
    Write a python program for the same. You can use your own python lists ?
"""

def main():
    # Define three lists
    list_1 = [1,2,3,44,5,90,781,888,1,2,30,234,72,59,46,4,0]
    list_2 = [9,8,4,5,5,10,767,8,5,6,7,8,555,35,42,12,9,0,6]
    list_3 = [4,11,34,89,21,5,2,0,0,0,0,0,23,91,11,1000]

    # Convert lists to sets to remove the duplicates in each list
    list_1, list_2, list_3 = set(list_1), set(list_2), set(list_3)

    # Finding the duplicates in the 3 lists
    duplicates = list(list_1 & list_2 & list_3)

    # Print result
    print("Duplicates in all three lists:", duplicates)

if __name__ == "__main__":
    main()