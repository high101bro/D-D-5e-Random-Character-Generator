#! /usr/bin/env python3

"""
Week 2
Everything is in Dis-Array
The jokester is back. Somehow, he got into a crucial dataset and mixed everything around.

Please help reorganize and put back together the data so that the disturbance will be made right and restore balance to these very complex datasets. Write a .py file that reads in the data, sorts it into a 20x20 array, and manipulate the data according to the steps dictated in the directions file. Your final submission will be the values in the main diagonal, separated by a comma and one(ONE, just one) space. For example a submission would look like 0, 1, 2, 3 for an array with that main diagonal.

Assumptions
The data should be read into an array that is 20 by 20.
Some of the indices for the updates may be out of range. If an index is out of range, skip that row of instructions
The submission will be the main diagonal after the final manipulation.
The directions are in the format x,y,z where x dictates whether you swap columns or rows, y is the index of the first column or row to swap, and z is the index of the second column or row to swap.
For example, row,1,2 informs that you would be replacing row one with row two and replacing row two with row one.
Initial Array
Read these values and create a 20x20 array that you will be manipulating. Initial Array

Directions
Use these directions to manipulate your array and return the final diagonal. Directions

Your Final Submission is the Main Diagonal of the Array After the Final Manipulation!!!! Read the prompt one more time to make sure you are submitting the correct information.
Suggested Functions
 - swap_cols(a,b,arr): swaps column a and column b of a given 2-d array
 - swap_rows(a,b,arr): swaps row a and row b of a given 2-d array
 
Write a function that swaps column a with column b given a 2-D array. Make sure to account for indices out of range for the array. If an index is out of range, skip that row of instructions.

# function starter
def swap_cols(a, b, arr):
    '''
    Returns the array after making the requested adjustments.
    
        Parameters:
            a (int): the location of the first column to be swapped
            b (int): the location of the second column to be swapped
            arr (array): the array that will be manipulated
            
        Returns:
            fixed_arr (arr): the manipulated array
    '''

    pass

Write a function that swaps row a with row b given a 2-D array. Make sure to account for indices that are out of range for the array. If an index is out of range, skip that row of instructions.

# function starter
def swap_rows(a, b, arr):
    '''
    Returns the array after making the requested adjustments.
    
        Parameters:
            a (int): the location of the first row to be swapped
            b (int): the location of the second row to be swapped
            arr (array): the array that will be manipulated
            
        Returns:
            fixed_arr (arr): the manipulated array
    '''

    pass


intiial_array= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399]

steps = [
row,16,1
column,4,3
row,6,12
column,8,19
row,1,8
column,15,9
row,18,8
column,19,7
row,18,13
column,12,1
row,7,14
column,3,20
row,6,45
column,8,3
row,6,15
column,14,7
row,2,9
column,1,22
row,13,20
column,6,12
row,8,14
column,10,12
row,2,3
column,9,8
]
"""

import numpy as np

array = np.genfromtxt('initial-array.csv', delimiter=',')
array = np.array(array)
array = array.reshape(20,20)
# print(array)



def swap_cols(a, b, arr):
    '''
    Returns the array after making the requested adjustments.
    
        Parameters:
            a (int): the location of the first column to be swapped
            b (int): the location of the second column to be swapped
            arr (array): the array that will be manipulated
            
        Returns:
            fixed_arr (arr): the manipulated array
    '''
    # print(f"col: {arr}")
    # print(f"swap 1: {a}")
    # print(f"swap 2: {b}")
    array[:, [a, b]] = array[:, [b, a]]
    return array


def swap_rows(a, b, arr):
    '''
    Returns the array after making the requested adjustments.
    
        Parameters:
            a (int): the location of the first row to be swapped
            b (int): the location of the second row to be swapped
            arr (array): the array that will be manipulated
            
        Returns:
            fixed_arr (arr): the manipulated array
    '''

    # print(f"row: {arr}")
    # print(f"swap 1: {a}")
    # print(f"swap 2: {b}")

    # Swapping columns
    array[[a, b], :] = array[[b, a], :]
    return array

# read in directions
with open('steps.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    # print(lines)
    for direction in lines:
        direction = direction.split(',')
        # print(direction)
        a = int(direction[1])
        b = int(direction[2])
        arr = direction[0]
        # print('--------')
        print(a)
        print(b)
        # print(arr)
        try:
            if arr == 'column':
                swap_cols(a, b, arr)
            elif arr == 'row':
                swap_rows(a, b, arr)
        except:
            pass
# print(array)

#apparently i misunderstood what a main diagon is...
# line = 0
# diagonal = []
# for row in array:
#     diagonal.append(int(row[line]))
#     line += 1
# print(diagonal) # still not what they want


main_diagonal = np.diag(array)
# print(main_diagonal) # still not what they want

diagonal_string = ', '.join(map(str, main_diagonal))
# print(diagonal_string) #need to remove .'s
diagonal_string = diagonal_string.replace('.0', '')
print(diagonal_string)

