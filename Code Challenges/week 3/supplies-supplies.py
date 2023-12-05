#! /usr/bin/env python3

"""
Week 3
Supplies, Supplies
The AI2C used up their reserve of shipping material during the last PC, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of the stuff they plan on shipping out to the desert next time, and want to order exactly as much material as they need.

Fortunately, every package is a box (a perfect right rectangular prism), which makes calculating the required packaging material for each thing a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. They also need a little extra material for each package (just in case): the area of the smallest side.

For Example
A package with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of packaging plus 6 square feet of slack, for a total of 58 square feet.
A package with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of packaging plus 1 square foot of slack, for a total of 43 square feet.
Surprise, surprise, we also ran out of tape... Tape is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The tape required to close these packages is the longest distance around its sides, or the largest perimeter of any one face. Each package also requires an overage calculation as well; the feet of tape required for the overage is equal to the cubic feet of volume of the package.

For Example
A package with dimensions 2x3x4 requires 4+4+3+3 = 14 feet of tape to close the package plus 2x3x4 = 24 feet of tape for the overage, for a total of 38 feet.
A package with dimensions 1x1x10 requires 10+10+1+1 = 22 feet of tape to close the package plus 1x1x10 = 10 feet of tape for the overage, for a total of 32 feet.
Use this list of dimensions to calculate the packaging materials and tape requirements. Package Dimensions

All numbers in the list are in feet. Given a list of the dimensions, determine how many total square feet of shipping material should they order and how many total linear feet of tape should they order. Submit your answer as the material shipping total and tape total separated by a space and a comma. 100 feet of material and 50 feet of tape would be 100, 50.

Assumptions
The dimensions will be given as a list of strings of the format: 'lxwxh'
For example, a 2 ft by 3 ft by 4 ft box will be listed as '2x3x4'
Sanity Checks
'2x3x4' should result in 58 square feet of packaging materials and 38 linear feet of tape
['2x3x4', '1x1x10'] should result in 101 square feet of packaging materials and 70 linear feet of tape
Remember, the final solution is the total amount of packaging material and tape that is needed to prepare the list of packages in the format material_total, tape_total.
Suggested Functions
- package_calc(dimensions): returns the total square footage needed for all packaging
- tape_calc(dimensinons): returns the total linear footage needed for all tape
Calculating Shipping Materials

def package_calc(dimensions):
    '''
    Returns the total square footage that is required for the list of packages.
    
        Parameters:
            dimensions(list): a list of strings, where each string is the dimensions of a package in the format 'lxwxh'
            
        Returns:
            total_material(int): an integer value for the total square footage needed to ship the packages.
    '''

    pass

Calculating Tape

def tape_calc(dimensions):
    '''
    Returns the total linear footage that is required to tape up the list of packages.
    
        Parameters:
            dimensions(list): a list of strings, where each string is the dimensions of a package in the format 'lxwxh'
            
        Returns:
            total_material(int): an integer value for the total linear footage of tape needed to secure the packages.
    '''

    pass
"""

def tape_calc(dimensions):
    '''
    Returns the total linear footage that is required to tape up the list of packages.
    
        Parameters:
            dimensions(list): a list of strings, where each string is the dimensions of a package in the format 'lxwxh'
            
        Returns:
            total_material(int): an integer value for the total linear footage of tape needed to secure the packages.
    '''

    pass

with open('file.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    # print(lines)
    total_tape = 0
    total_material = 0
    for line in lines:
        dimensions = line.split('x')
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])
        smallest_side = min([length,width,height])
        print(length,width,height)
        # print(smallest_side)
        perimeter = 2 * (length + width)
        # overage = length * width * height
        # tape = perimeter + overage
        tape = perimeter + smallest_side
        total_tape += tape
        # total_material += overage
        total_material += smallest_side
    print("Total linear footage of tape needed: ", total_tape)
    print("Total square footage of material needed: ", total_material)
    print(f"{total_material}, {total_tape}")
